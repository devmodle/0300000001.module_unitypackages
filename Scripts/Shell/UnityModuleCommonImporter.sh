#/bin/bash
oProjName=${1}
oBranchName=${2}

oSubmodules=(".UnityModule.Common" 
	".UnityModule.Common.Define" 
	".UnityModule.Common.Utility" 
	".UnityModule.Common.Access" 
	".UnityModule.Common.Func" 
	".UnityModule.Common.Factory" 
	".UnityModule.Common.Extension" 
	".UnityModule.Common.Externals" 
	".UnityModule.Common.Ads" 
	".UnityModule.Common.Flurry" 
	".UnityModule.Common.Tenjin" 
	".UnityModule.Common.Facebook" 
	".UnityModule.Common.Firebase" 
	".UnityModule.Common.UnityService" 
	".UnityModule.Common.Singular" 
	".UnityModule.Common.GameCenter" 
	".UnityModule.Common.Purchase")

oSubmodulePaths=("${oProjName}/Packages" 
	"${oProjName}/Packages" 
	"${oProjName}/Packages" 
	"${oProjName}/Packages" 
	"${oProjName}/Packages" 
	"${oProjName}/Packages" 
	"${oProjName}/Packages" 
	"${oProjName}/Packages" 
	"${oProjName}/Packages" 
	"${oProjName}/Packages" 
	"${oProjName}/Packages" 
	"${oProjName}/Packages" 
	"${oProjName}/Packages" 
	"${oProjName}/Packages" 
	"${oProjName}/Packages" 
	"${oProjName}/Packages" 
	"${oProjName}/Packages")

oSubmoduleURLs=("https://gitlab.com/9tapmodule.repository/unitymodule_common_client.git" 
	"https://gitlab.com/9tapmodule.repository/unitymodule_common_define_client.git" 
	"https://gitlab.com/9tapmodule.repository/unitymodule_common_utility_client.git" 
	"https://gitlab.com/9tapmodule.repository/unitymodule_common_access_client.git" 
	"https://gitlab.com/9tapmodule.repository/unitymodule_common_func_client.git" 
	"https://gitlab.com/9tapmodule.repository/unitymodule_common_factory_client.git" 
	"https://gitlab.com/9tapmodule.repository/unitymodule_common_extension_client.git" 
	"https://gitlab.com/9tapmodule.repository/unitymodule_common_externals_client.git" 
	"https://gitlab.com/9tapmodule.repository/unitymodule_common_ads_client.git" 
	"https://gitlab.com/9tapmodule.repository/unitymodule_common_flurry_client.git" 
	"https://gitlab.com/9tapmodule.repository/unitymodule_common_tenjin_client.git" 
	"https://gitlab.com/9tapmodule.repository/unitymodule_common_facebook_client.git" 
	"https://gitlab.com/9tapmodule.repository/unitymodule_common_firebase_client.git" 
	"https://gitlab.com/9tapmodule.repository/unitymodule_common_unityservice_client.git" 
	"https://gitlab.com/9tapmodule.repository/unitymodule_common_singular_client.git" 
	"https://gitlab.com/9tapmodule.repository/unitymodule_common_gamecenter_client.git" 
	"https://gitlab.com/9tapmodule.repository/unitymodule_common_purchase_client.git")

for ((i = 0; i < ${#oSubmodules[@]}; ++i)); do
	if [ ! -d "../../${oSubmodulePaths[$i]}/${oSubmodules[$i]}" ]; then
		if [ ! -d "../../${oSubmodulePaths[$i]}" ]; then
			mkdir -p "../../${oSubmodulePaths[$i]}"
		fi

		git submodule add -f "${oSubmoduleURLs[$i]}" "../../${oSubmodulePaths[$i]}/${oSubmodules[$i]}"
	fi

	git submodule set-branch --branch "${oBranchName}" "${oSubmodulePaths[$i]}/${oSubmodules[$i]}"
done
