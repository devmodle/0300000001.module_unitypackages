import os
import sys

oProjName = sys.argv[1]
oBranchName = sys.argv[2]

oSubmoduleInfos = [
	{
		"Name" : "PluginProjects",
		"Path" : oProjName,
		"URL" : "https://gitlab.com/9tapmodule.repository/unitymodule_plugin_client.git"
	},

	{
		"Name" : "UnityPackages",
		"Path" : oProjName,
		"URL" : "https://gitlab.com/9tapmodule.repository/unitymodule_package_client.git"
	}
]

for oSubmoduleInfo in oSubmoduleInfos:
	oURL = oSubmoduleInfo["URL"]
	oPath = os.path.join("..", "..", oSubmoduleInfo["Path"])
	oFullpath = os.path.join("..", "..", oSubmoduleInfo["Path"], oSubmoduleInfo["Name"])

	if not os.path.exists(oFullpath):
		if not os.path.exists(oPath):
			os.makedir(oPath)

		os.system(f"git submodule add -f {oURL} {oFullpath}")

	oSubmodulePath = os.path.join(oSubmoduleInfo["Path"], oSubmoduleInfo["Name"])
	os.system(f"git submodule set-branch --branch {oBranchName} {oSubmodulePath}")
