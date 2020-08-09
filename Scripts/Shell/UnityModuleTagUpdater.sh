#/bin/bash
oProjName=${1}
oTagName=${2}
oCurrentPath=$(pwd)

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
	".UnityModule.Common.Importer")

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
	"${oProjName}/Packages")

for ((i = 0; i < ${#oSubmodules[@]}; ++i)); do
	if [ -d "../../${oSubmodulePaths[$i]}/${oSubmodules[$i]}" ]; then
		cd "../../${oSubmodulePaths[$i]}/${oSubmodules[$i]}"

		git tag -d ${oTagName}; git push origin --delete ${oTagName}
		git tag ${oTagName}; git push origin --tags

		cd ${oCurrentPath}
	fi
done
