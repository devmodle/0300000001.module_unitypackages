#/bin/bash
oProjName=${1}
oBranchName=${2}

oSubmodules=(".UnityModule.Study" ".UnityModule.Study.Define" ".UnityModule.Study.Utility")
oSubmodulePaths=("${oProjName}/Packages" "${oProjName}/Packages" "${oProjName}/Packages")

oSubmoduleURLs=("https://gitlab.com/dante.distribution.individual/unitymodule_study_client.git" 
	"https://gitlab.com/dante.distribution.individual/unitymodule_study_define_client.git" 
	"https://gitlab.com/dante.distribution.individual/unitymodule_study_utility_client.git")

for ((i = 0; i < ${#oSubmodules[@]}; ++i)); do
	if [ ! -d "../../${oSubmodulePaths[$i]}/${oSubmodules[$i]}" ]; then
		if [ ! -d "../../${oSubmodulePaths[$i]}" ]; then
			mkdir -p "../../${oSubmodulePaths[$i]}"
		fi

		git submodule add -f "${oSubmoduleURLs[$i]}" "../../${oSubmodulePaths[$i]}/${oSubmodules[$i]}"
	fi

	git submodule set-branch --branch "${oBranchName}" "${oSubmodulePaths[$i]}/${oSubmodules[$i]}"
done

./UnityModuleCommonImporter.sh ${oProjName} ${oBranchName}
