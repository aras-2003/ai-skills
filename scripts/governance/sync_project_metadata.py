#!/usr/bin/env python3
"""Sync existing GitHub Issues to Project V2 fields. Never create project items or mutate Issues."""
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

PROJECT = """query($owner:String!, $project:Int!, $repo:String!, $issue:Int!) {
  user(login:$owner) {
    projectV2(number:$project) {
      id
      fields(first:100) {nodes {
        ... on ProjectV2SingleSelectField {id name options{id name}}
      }}
    }
    repository(name:$repo) {
      issue(number:$issue) {
        title body labels(first:100) {nodes{name}}
        projectItems(first:100) {nodes{id project{id number}}}
      }
    }
  }
}"""
# GitHub's user->repository works for own user repositories only.
UPDATE = """mutation($project:ID!, $item:ID!, $field:ID!, $option:String!) {
  updateProjectV2ItemFieldValue(input:{
    projectId:$project,itemId:$item,fieldId:$field,
    value:{singleSelectOptionId:$option}
  }) {projectV2Item{id}}
}"""
PRIORITY = {"P0", "P1", "P2", "P3"}
SIZE = {"XS", "S", "M", "L", "XL"}
AREA = {"Engineering", "Runtime", "E2E & Quality", "Security", "Commerce",
        "Investing", "OAF", "Learning", "Strategy", "Other"}
PREFIX_AREA = {"ENG":"Engineering", "E2E":"E2E & Quality",
               "STR":"Strategy", "LEA":"Learning", "DOM":"Engineering",
               "PRO":"Other", "LIF":"Other", "CON":"Other", "WRI":"Other",
               "CORE":"Engineering", "EXI":"Engineering"}

def gql(query, variables):
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query":query, "variables":variables}).encode(),
        headers={"Authorization":"Bearer " + os.environ["PROJECTS_TOKEN"],
                 "Accept":"application/vnd.github+json",
                 "Content-Type":"application/json",
                 "X-GitHub-Api-Version":"2022-11-28"},
        method="POST")
    try:
        with urllib.request.urlopen(req, timeout=25) as response:
            result = json.load(response)
    except urllib.error.HTTPError as exc:
        raise RuntimeError(f"GraphQL HTTP {exc.code}") from exc
    if result.get("errors"):
        raise RuntimeError("GitHub GraphQL error: " + json.dumps(result["errors"]))
    return result["data"]

def values(title, body, labels):
    """Strict fields from labels, or legacy exact key syntax. Never guess missing values."""
    labels = {x.lower() for x in labels}
    result = {}
    for field, valid, pattern in (
        ("Priority", PRIORITY, r"(?mi)^-?\s*(?:historical )?priority\s*:\s*\*{0,2}(P[0-3])\b"),
        ("Size", SIZE, r"(?mi)^-?\s*(?:size|effort)\s*:\s*\*{0,2}(XS|S|M|L|XL)\b"),
        ("Area", AREA, None)):
        selected = [v for v in valid if f"{field.lower()}:{v.lower()}" in labels]
        if len(selected) > 1:
            raise ValueError(f"Conflicting {field} labels: {selected}")
        if selected:
            result[field] = selected[0]
        elif pattern:
            m = re.search(pattern, body)
            if m:
                result[field] = m.group(1)
    if "Area" not in result:
        m = re.match(r"^\[([A-Z]+)-\d+\]", title)
        if m:
            result["Area"] = PREFIX_AREA.get(m.group(1), "Other")
    return result

def main():
    repo = os.environ["GH_REPOSITORY"]
    owner = os.environ["PROJECT_OWNER"]
    number = int(os.environ["PROJECT_NUMBER"])
    issue = int(os.environ["ISSUE_NUMBER"])
    if repo != f"{owner}/skills-factory":
        raise RuntimeError("Unexpected repository; refusing cross-repository mutation")
    data = None
    for attempt in range(6):
        data = gql(PROJECT, {"owner":owner,"project":number,"repo":"skills-factory","issue":issue})
        user = data.get("user") or {}
        project = user.get("projectV2")
        obj = (user.get("repository") or {}).get("issue")
        if not project or not obj:
            raise RuntimeError("Project or issue not accessible")
        items = [n for n in obj["projectItems"]["nodes"] if n["project"]["id"] == project["id"]]
        if items: break
        if attempt < 5: time.sleep(10)
    else:
        raise RuntimeError("Issue not in Project yet (auto-add pending/failed); refusing to report success")
    if len(items) != 1:
        raise RuntimeError("Ambiguous Project items")
    target = values(obj["title"], obj.get("body") or "", [n["name"] for n in obj["labels"]["nodes"]])
    fields = {x["name"]:x for x in project["fields"]["nodes"] if x and x.get("name")}
    if not target:
        print("No explicit metadata; no changes")
        return
    for name, value in target.items():
        f = fields.get(name)
        if not f or "options" not in f:
            raise RuntimeError(f"Required Project field {name} missing or not single-select")
        options = [o["id"] for o in f["options"] if o["name"].casefold()==value.casefold()]
        if len(options)!=1:
            raise RuntimeError(f"Option {value} missing/ambiguous for {name}")
        gql(UPDATE, {"project":project["id"],"item":items[0]["id"],
                     "field":f["id"],"option":options[0]})
        print(f"Set {name}={value} on Project #{number} Issue #{issue}")

if __name__ == "__main__":
    try: main()
    except (ValueError, RuntimeError, KeyError, urllib.error.URLError) as error:
        print(f"::error::{error}",file=sys.stderr)
        sys.exit(1)
