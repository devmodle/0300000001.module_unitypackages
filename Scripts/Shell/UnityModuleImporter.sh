#/bin/bash
oProjName=${1}
oBranchName=${2}

oSubmodules=(".UnityModule.Study.Importer" ".UnityModule.Common.Importer")
oSubmodulePaths=("${oProjName}/Packages" "${oProjName}/Packages")
oSubmoduleURLs=("https://gitlab.com/dante.distribution.individual/unitymodule_study_importer_client.git" "https://gitlab.com/9tapmodule.repository/unitymodule_common_importer_client.git")

for ((i = 0; i < ${#oSubmodules[@]}; ++i)); do
	if [ ! -d "../../${oSubmodulePaths[$i]}/${oSubmodules[$i]}" ]; then
		if [ ! -d "../../${oSubmodulePaths[$i]}" ]; then
			mkdir -p "../../${oSubmodulePaths[$i]}"
		fi

		git submodule add -f "${oSubmoduleURLs[$i]}" "../../${oSubmodulePaths[$i]}/${oSubmodules[$i]}"
	fi

	git submodule set-branch --branch "${oBranchName}" "${oSubmodulePaths[$i]}/${oSubmodules[$i]}"
done

./UnityModuleStudyImporter.sh ${oProjName} ${oBranchName}
./UnityModuleCommonImporter.sh ${oProjName} ${oBranchName}
./UnityModulePluginImporter.sh ${oProjName} ${oBranchName}
