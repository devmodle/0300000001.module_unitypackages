#/bin/bash
oProjName=${1}
oBranchName=${2}

oSubmodules=("PluginProjects" "UnityPackages")
oSubmodulePaths=("${oProjName}" "${oProjName}")

oSubmoduleURLs=("https://gitlab.com/9tapmodule.repository/unitymodule_plugin_client.git"
	"https://gitlab.com/9tapmodule.repository/unitymodule_package_client.git")

for ((i = 0; i < ${#oSubmodules[@]}; ++i)); do
	if [ ! -d "../../${oSubmodulePaths[$i]}/${oSubmodules[$i]}" ]; then
		if [ ! -d "../../${oSubmodulePaths[$i]}" ]; then
			mkdir -p "../../${oSubmodulePaths[$i]}"
		fi

		git submodule add -f "${oSubmoduleURLs[$i]}" "../../${oSubmodulePaths[$i]}/${oSubmodules[$i]}"
	fi

	git submodule set-branch --branch "${oBranchName}" "${oSubmodulePaths[$i]}/${oSubmodules[$i]}"
done
