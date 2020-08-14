import os
import sys

oProjName = sys.argv[1]

oSubmoduleInfos = [
	{
		"Name" : ".UnityModule.Study",
		"Path" : os.path.join(oProjName, "Packages")
	},

	{
		"Name" : ".UnityModule.Study.Define",
		"Path" : os.path.join(oProjName, "Packages")
	},

	{
		"Name" : ".UnityModule.Study.Utility",
		"Path" : os.path.join(oProjName, "Packages")
	},

	{
		"Name" : ".UnityModule.Study.Importer",
		"Path" : os.path.join(oProjName, "Packages")
	},

	{
		"Name" : ".UnityModule.Common",
		"Path" : os.path.join(oProjName, "Packages")
	},

	{
		"Name" : ".UnityModule.Common.Define",
		"Path" : os.path.join(oProjName, "Packages")
	},

	{
		"Name" : ".UnityModule.Common.Access",
		"Path" : os.path.join(oProjName, "Packages")
	},

	{
		"Name" : ".UnityModule.Common.Factory",
		"Path" : os.path.join(oProjName, "Packages")
	},

	{
		"Name" : ".UnityModule.Common.Extension",
		"Path" : os.path.join(oProjName, "Packages")
	},

	{
		"Name" : ".UnityModule.Common.Func",
		"Path" : os.path.join(oProjName, "Packages")
	},

	{
		"Name" : ".UnityModule.Common.Utility",
		"Path" : os.path.join(oProjName, "Packages")
	},
	
	{
		"Name" : ".UnityModule.Common.Externals",
		"Path" : os.path.join(oProjName, "Packages")
	},

	{
		"Name" : ".UnityModule.Common.Ads",
		"Path" : os.path.join(oProjName, "Packages")
	},

	{
		"Name" : ".UnityModule.Common.Flurry",
		"Path" : os.path.join(oProjName, "Packages")
	},

	{
		"Name" : ".UnityModule.Common.Tenjin",
		"Path" : os.path.join(oProjName, "Packages")
	},

	{
		"Name" : ".UnityModule.Common.Facebook",
		"Path" : os.path.join(oProjName, "Packages")
	},

	{
		"Name" : ".UnityModule.Common.Firebase",
		"Path" : os.path.join(oProjName, "Packages")
	},

	{
		"Name" : ".UnityModule.Common.UnityService",
		"Path" : os.path.join(oProjName, "Packages")
	},

	{
		"Name" : ".UnityModule.Common.Singular",
		"Path" : os.path.join(oProjName, "Packages")
	},

	{
		"Name" : ".UnityModule.Common.GameCenter",
		"Path" : os.path.join(oProjName, "Packages")
	},

	{
		"Name" : ".UnityModule.Common.Purchase",
		"Path" : os.path.join(oProjName, "Packages")
	},

	{
		"Name" : ".UnityModule.Common.Importer",
		"Path" : os.path.join(oProjName, "Packages")
	},

	{
		"Name" : "PluginProjects",
		"Path" : oProjName
	},

	{
		"Name" : "UnityPackages",
		"Path" : oProjName
	}
]

for oSubmoduleInfo in oSubmoduleInfos:
	oPath = os.path.join("..", "..", oSubmoduleInfo["Path"], oSubmoduleInfo["Name"])
	oCurrentPath = os.getcwd()

	if os.path.exists(oPath):
		os.chdir(oPath)

		os.system("git fetch")
		os.system("git pull -p")

		os.chdir(oCurrentPath)
