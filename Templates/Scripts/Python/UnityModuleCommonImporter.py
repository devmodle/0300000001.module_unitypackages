import os
import sys

oProjRoot = sys.argv[1]
oProjName = sys.argv[2]
oBranchName = sys.argv[3]

oSubmoduleInfos = [
	{
		"Name": ".UnityModule.Common",
		"Path": f"{oProjName}/Packages",
		"URL": "https://gitlab.com/9tapmodule.repository/000001.module_unitycommon_client.git"
	},

	{
		"Name": ".UnityModule.Common.Define",
		"Path": f"{oProjName}/Packages",
		"URL": "https://gitlab.com/9tapmodule.repository/000001.module_unitycommondefine_client.git"
	},

	{
		"Name": ".UnityModule.Common.Access",
		"Path": f"{oProjName}/Packages",
		"URL": "https://gitlab.com/9tapmodule.repository/000001.module_unitycommonaccess_client.git"
	},

	{
		"Name": ".UnityModule.Common.Factory",
		"Path": f"{oProjName}/Packages",
		"URL": "https://gitlab.com/9tapmodule.repository/000001.module_unitycommonfactory_client.git"
	},

	{
		"Name": ".UnityModule.Common.Extension",
		"Path": f"{oProjName}/Packages",
		"URL": "https://gitlab.com/9tapmodule.repository/000001.module_unitycommonextension_client.git"
	},

	{
		"Name": ".UnityModule.Common.Func",
		"Path": f"{oProjName}/Packages",
		"URL": "https://gitlab.com/9tapmodule.repository/000001.module_unitycommonfunc_client.git"
	},

	{
		"Name": ".UnityModule.Common.Utility",
		"Path": f"{oProjName}/Packages",
		"URL": "https://gitlab.com/9tapmodule.repository/000001.module_unitycommonutility_client.git"
	},

	{
		"Name": ".UnityModule.Common.Externals",
		"Path": f"{oProjName}/Packages",
		"URL": "https://gitlab.com/9tapmodule.repository/000001.module_unitycommonexternals_client.git"
	},

	{
		"Name": ".UnityModule.Common.Ads",
		"Path": f"{oProjName}/Packages",
		"URL": "https://gitlab.com/9tapmodule.repository/000001.module_unitycommonads_client.git"
	},

	{
		"Name": ".UnityModule.Common.Flurry",
		"Path": f"{oProjName}/Packages",
		"URL": "https://gitlab.com/9tapmodule.repository/000001.module_unitycommonflurry_client.git"
	},
	
	{
		"Name": ".UnityModule.Common.Facebook",
		"Path": f"{oProjName}/Packages",
		"URL": "https://gitlab.com/9tapmodule.repository/000001.module_unitycommonfacebook_client.git"
	},

	{
		"Name": ".UnityModule.Common.Firebase",
		"Path": f"{oProjName}/Packages",
		"URL": "https://gitlab.com/9tapmodule.repository/000001.module_unitycommonfirebase_client.git"
	},

	{
		"Name": ".UnityModule.Common.GameAnalytics",
		"Path": f"{oProjName}/Packages",
		"URL": "https://gitlab.com/9tapmodule.repository/000001.module_unitycommongameanalytics_client.git"
	},
	
	{
		"Name": ".UnityModule.Common.Singular",
		"Path": f"{oProjName}/Packages",
		"URL": "https://gitlab.com/9tapmodule.repository/000001.module_unitycommonsingular_client.git"
	},

	{
		"Name": ".UnityModule.Common.GameCenter",
		"Path": f"{oProjName}/Packages",
		"URL": "https://gitlab.com/9tapmodule.repository/000001.module_unitycommongamecenter_client.git"
	},

	{
		"Name": ".UnityModule.Common.Purchase",
		"Path": f"{oProjName}/Packages",
		"URL": "https://gitlab.com/9tapmodule.repository/000001.module_unitycommonpurchase_client.git"
	},

	{
		"Name": ".UnityModule.Common.Noti",
		"Path": f"{oProjName}/Packages",
		"URL": "https://gitlab.com/9tapmodule.repository/000001.module_unitycommonnoti_client.git"
	}
]

for oSubmoduleInfo in oSubmoduleInfos:
	oURL = oSubmoduleInfo["URL"]
	oPath = f"../../{oSubmoduleInfo['Path']}"
	oFullpath = f"../../{oSubmoduleInfo['Path']}/{oSubmoduleInfo['Name']}"

	if not os.path.exists(oFullpath):
		if not os.path.exists(oPath):
			os.makedirs(oPath)

		os.system(f"git submodule add -f {oURL} {oFullpath}")

	oSubmodulePath = f"{oSubmoduleInfo['Path']}/{oSubmoduleInfo['Name']}"

	# 프로젝트 루트가 유효 할 경우
	if len(oProjRoot) >= 1:
		os.system(f"git submodule set-branch --branch {oBranchName} {oProjRoot}/{oSubmodulePath}")
	else:
		os.system(f"git submodule set-branch --branch {oBranchName} {oSubmodulePath}")

os.system(f"python3 UnityModuleRemoteURLUpdater.py {oProjName}")
