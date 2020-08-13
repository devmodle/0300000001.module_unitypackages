import os
import sys

oProjName = sys.argv[1]
oBranchName = sys.argv[2]

oSubmoduleInfos = [
	{
		"Name" : ".UnityModule.Study",
		"Path" : os.path.join(oProjName, "Packages"),
		"URL" : "https://gitlab.com/dante.distribution.individual/unitymodule_study_client.git"
	},

	{
		"Name" : ".UnityModule.Study.Define",
		"Path" : os.path.join(oProjName, "Packages"),
		"URL" : "https://gitlab.com/dante.distribution.individual/unitymodule_study_define_client.git"
	},

	{
		"Name" : ".UnityModule.Study.Utility",
		"Path" : os.path.join(oProjName, "Packages"),
		"URL" : "https://gitlab.com/dante.distribution.individual/unitymodule_study_utility_client.git"
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

os.system(f"python3 UnityModuleCommonImporter.py {oProjName} {oBranchName}")
