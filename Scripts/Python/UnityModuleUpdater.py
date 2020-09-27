import os
import sys

oProjName = sys.argv[1]

oSubmoduleInfos = [
	{
		"Name": ".UnityModule.Study",
		"Path": f"{oProjName}/Packages"
	},

	{
		"Name": ".UnityModule.Study.Define",
		"Path": f"{oProjName}/Packages"
	},

	{
		"Name": ".UnityModule.Study.Utility",
		"Path": f"{oProjName}/Packages"
	},

	{
		"Name": ".UnityModule.Study.Importer",
		"Path": f"{oProjName}/Packages"
	},

	{
		"Name": ".UnityModule.Common",
		"Path": f"{oProjName}/Packages"
	},

	{
		"Name": ".UnityModule.Common.Define",
		"Path": f"{oProjName}/Packages"
	},

	{
		"Name": ".UnityModule.Common.Access",
		"Path": f"{oProjName}/Packages"
	},

	{
		"Name": ".UnityModule.Common.Factory",
		"Path": f"{oProjName}/Packages"
	},

	{
		"Name": ".UnityModule.Common.Extension",
		"Path": f"{oProjName}/Packages"
	},

	{
		"Name": ".UnityModule.Common.Func",
		"Path": f"{oProjName}/Packages"
	},

	{
		"Name": ".UnityModule.Common.Utility",
		"Path": f"{oProjName}/Packages"
	},
	
	{
		"Name": ".UnityModule.Common.Externals",
		"Path": f"{oProjName}/Packages"
	},

	{
		"Name": ".UnityModule.Common.Ads",
		"Path": f"{oProjName}/Packages"
	},

	{
		"Name": ".UnityModule.Common.Flurry",
		"Path": f"{oProjName}/Packages"
	},

	{
		"Name": ".UnityModule.Common.Tenjin",
		"Path": f"{oProjName}/Packages"
	},

	{
		"Name": ".UnityModule.Common.Facebook",
		"Path": f"{oProjName}/Packages"
	},

	{
		"Name": ".UnityModule.Common.Firebase",
		"Path": f"{oProjName}/Packages"
	},

	{
		"Name": ".UnityModule.Common.UnityService",
		"Path": f"{oProjName}/Packages"
	},

	{
		"Name": ".UnityModule.Common.Singular",
		"Path": f"{oProjName}/Packages"
	},

	{
		"Name": ".UnityModule.Common.GameCenter",
		"Path": f"{oProjName}/Packages"
	},

	{
		"Name": ".UnityModule.Common.Purchase",
		"Path": f"{oProjName}/Packages"
	},

	{
		"Name": ".UnityModule.Common.LocalNoti",
		"Path": f"{oProjName}/Packages"
	},

	{
		"Name": ".UnityModule.Common.Importer",
		"Path": f"{oProjName}/Packages"
	},

	{
		"Name": "PluginProjects",
		"Path": oProjName
	},

	{
		"Name": "UnityPackages",
		"Path": oProjName
	}
]

for oSubmoduleInfo in oSubmoduleInfos:
	oPath = f"../../{oSubmoduleInfo['Path']}/{oSubmoduleInfo['Name']}"
	oCurrentPath = os.getcwd()

	if os.path.exists(oPath):
		os.chdir(oPath)

		os.system("git fetch")
		os.system("git pull -p")

		os.chdir(oCurrentPath)
