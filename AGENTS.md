# Skills Factory agent instructions

For publication of the existing Skills Factory Cloud Next Site, read `docs/SITES-PUBLISHING.md` and the installed Sites hosting skill before executing. A user request to publish authorizes ordinary checks, source synchronization and private deployment; platform approval review remains applicable.

GitHub source and the Sites source repository are separate. GitHub main updates do not publish the Site. Use the Sites plugin's official workflow and native deployment tools. Sandbox DNS failure alone is not an approval rejection; follow the documented local network approval path and describe credential delivery through hidden stdin explicitly.

Preserve source history, Site/plugin identity and the current audience. Report actual deployed version and revision; keep embedded Lab revision separate from Site source revision. For Chat functional tests, explicitly select the Cloud Next plugin and verify actual tool invocation.
