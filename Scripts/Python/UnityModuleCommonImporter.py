import os
import sys

oProjName = sys.argv[1]
oBranchName = sys.argv[2]

oSubmoduleInfos = [
	{
		"Name" : ".UnityModule.Common",
		"Path" : os.path.join(oProjName, "Packages"),
		"URL" : "https://gitlab.com/9tapmodule.repository/unitymodule_common_client.git"
	},

	{
		"Name" : ".UnityModule.Common.Define",
		"Path" : os.path.join(oProjName, "Packages"),
		"URL" : "https://gitlab.com/9tapmodule.repository/unitymodule_common_define_client.git"
	},

	{
		"Name" : ".UnityModule.Common.Access",
		"Path" : os.path.join(oProjName, "Packages"),
		"URL" : "https://gitlab.com/9tapmodule.repository/unitymodule_common_access_client.git"
	},

	{
		"Name" : ".UnityModule.Common.Factory",
		"Path" : os.path.join(oProjName, "Packages"),
		"URL" : "https://gitlab.com/9tapmodule.repository/unitymodule_common_factory_client.git"
	},

	{
		"Name" : ".UnityModule.Common.Extension",
		"Path" : os.path.join(oProjName, "Packages"),
		"URL" : "https://gitlab.com/9tapmodule.repository/unitymodule_common_extension_client.git"
	},

	{
		"Name" : ".UnityModule.Common.Func",
		"Path" : os.path.join(oProjName, "Packages"),
		"URL" : "https://gitlab.com/9tapmodule.repository/unitymodule_common_func_client.git"
	},

	{
		"Name" : ".UnityModule.Common.Utility",
		"Path" : os.path.join(oProjName, "Packages"),
		"URL" : "https://gitlab.com/9tapmodule.repository/unitymodule_common_utility_client.git"
	},

	{
		"Name" : ".UnityModule.Common.Externals",
		"Path" : os.path.join(oProjName, "Packages"),
		"URL" : "https://gitlab.com/9tapmodule.repository/unitymodule_common_externals_client.git"
	},

	{
		"Name" : ".UnityModule.Common.Ads",
		"Path" : os.path.join(oProjName, "Packages"),
		"URL" : "https://gitlab.com/9tapmodule.repository/unitymodule_common_ads_client.git"
	},

	{
		"Name" : ".UnityModule.Common.Flurry",
		"Path" : os.path.join(oProjName, "Packages"),
		"URL" : "https://gitlab.com/9tapmodule.repository/unitymodule_common_flurry_client.git"
	},

	{
		"Name" : ".UnityModule.Common.Tenjin",
		"Path" : os.path.join(oProjName, "Packages"),
		"URL" : "https://gitlab.com/9tapmodule.repository/unitymodule_common_tenjin_client.git"
	},

	{
		"Name" : ".UnityModule.Common.Facebook",
		"Path" : os.path.join(oProjName, "Packages"),
		"URL" : "https://gitlab.com/9tapmodule.repository/unitymodule_common_facebook_client.git"
	},

	{
		"Name" : ".UnityModule.Common.Firebase",
		"Path" : os.path.join(oProjName, "Packages"),
		"URL" : "https://gitlab.com/9tapmodule.repository/unitymodule_common_firebase_client.git"
	},

	{
		"Name" : ".UnityModule.Common.UnityService",
		"Path" : os.path.join(oProjName, "Packages"),
		"URL" : "https://gitlab.com/9tapmodule.repository/unitymodule_common_unityservice_client.git"
	},

	{
		"Name" : ".UnityModule.Common.Singular",
		"Path" : os.path.join(oProjName, "Packages"),
		"URL" : "https://gitlab.com/9tapmodule.repository/unitymodule_common_singular_client.git"
	},

	{
		"Name" : ".UnityModule.Common.GameCenter",
		"Path" : os.path.join(oProjName, "Packages"),
		"URL" : "https://gitlab.com/9tapmodule.repository/unitymodule_common_gamecenter_client.git"
	},

	{
		"Name" : ".UnityModule.Common.Purchase",
		"Path" : os.path.join(oProjName, "Packages"),
		"URL" : "https://gitlab.com/9tapmodule.repository/unitymodule_common_purchase_client.git"
	},

	{
		"Name" : ".UnityModule.Common.LocalNoti",
		"Path" : os.path.join(oProjName, "Packages"),
		"URL" : "https://gitlab.com/9tapmodule.repository/unitymodule_common_localnoti_client.git"
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
