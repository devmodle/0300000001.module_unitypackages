import os
import sys

oParams = {
	"ProjPath": sys.argv[1],
	"Platform": sys.argv[2],
	"ProjPlatform": sys.argv[3],
	"BuildMode": sys.argv[4],
	"BuildFunc": sys.argv[5],
	"BuildFileExtension": sys.argv[6],
	"BundleID": sys.argv[7],
	"ProfileID": sys.argv[8],
	"IPAExportMethod": sys.argv[9]
}

oBuildOutputDirPath = f"{oParams["ProjPath"]}/{os.path.dirname(oParams["BuildOutputPath"])}"

for oPath, oDirNames, oFileNames in os.walk(oBuildOutputDirPath):
	for i, oFileName in enumerate(oFileNames):
		oSrcPath = f"{oPath}/{oFileName}"
		oDestPath = f"{oPath}/{oParams["Platform"]}BuildOutput.{oParams["BuildFileExtension"]}"

		# 빌드 결과가 존재 할 경우
		if os.path.exists(oSrcPath) and oSrcPath.lower().endswith(f".{oParams["BuildFileExtension"]}"):
			# 이전 빌드 결과가 존재 할 경우
			if os.path.exists(oDestPath):
				os.system(f"rm -rf \"{oDestPath}\"")

		os.system(f"mv \"{oSrcPath}\" \"{oDestPath}\"")
