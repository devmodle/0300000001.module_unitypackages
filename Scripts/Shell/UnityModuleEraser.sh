#/bin/bash
oProjName=${1}

oSubmodules=(".UnityModule.Study" 
	".UnityModule.Study.Define" 
	".UnityModule.Study.Utility" 
	".UnityModule.Study.Importer" 
	".UnityModule.Common" 
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
	".UnityModule.Common.Purchase" 
	".UnityModule.Common.Importer" 
	"PluginProjects" 
	"UnityPackages")

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
	"${oProjName}/Packages" 
	"${oProjName}/Packages" 
	"${oProjName}/Packages" 
	"${oProjName}/Packages" 
	"${oProjName}/Packages" 
	"${oProjName}/Packages" 
	"${oProjName}" 
	"${oProjName}")

for ((i = 0; i < ${#oSubmodules[@]}; ++i)); do
	if [ -d "../../${oSubmodulePaths[$i]}/${oSubmodules[$i]}" ]; then
		git submodule deinit -f "../../${oSubmodulePaths[$i]}/${oSubmodules[$i]}"
		git rm -f "../../${oSubmodulePaths[$i]}/${oSubmodules[$i]}"

		rm -rf "../../${oSubmodulePaths[$i]}/${oSubmodules[$i]}"
		rm -rf "../../.git/modules/${oSubmodulePaths[$i]}/${oSubmodules[$i]}"
	fi
done
