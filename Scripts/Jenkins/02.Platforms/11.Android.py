import os
import sys

oParams = {
	"ProjPath": sys.argv[1],
	"Platform": sys.argv[2],
	"ProjPlatform": sys.argv[3],
	"BuildFunc": sys.argv[4]
}

oBuildOutputDirPath = f"{oParams["ProjPath"]}/{os.path.dirname(oParams["BuildOutputPath"])}"

for oPath, oDirNames, oFileNames in os.walk(oBuildOutputDirPath):
	for i, oFileName in enumerate(oFileNames):
		oSrcPath = f"{oPath}/{oFileName}"
		oDestPath = f"{oPath}/{oParams["Platform"]}BuildOutputSymbols.zip"

		# 심볼 결과가 존재 할 경우
		if os.path.exists(oSrcPath) and oSrcPath.lower().endswith(".zip"):
			# 이전 심볼 결과가 존재 할 경우
			if os.path.exists(oDestPath):
				os.system(f"rm -rf \"{oDestPath}\"")

		os.system(f"mv \"{oSrcPath}\" \"{oDestPath}\"")
