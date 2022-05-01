import os
import sys

oProjPath = sys.argv[1]
oPlatform = sys.argv[2]
oBuildOutputPath = sys.argv[3]
oBuildFileExtension = sys.argv[4]

oBuildOutputDirPath = f"{oProjPath}/{os.path.dirname(oBuildOutputPath)}"

for oPath, oDirNames, oFileNames in os.walk(oBuildOutputDirPath):
	for i, oFileName in enumerate(oFileNames):
		oSrcPath = f"{oPath}/{oFileName}"
		oDestPath = f"{oPath}/{oPlatform}BuildOutput.{oBuildFileExtension}"

		# 빌드 결과가 존재 할 경우
		if os.path.exists(oSrcPath) and oSrcPath.lower().endswith(f".{oBuildFileExtension}"):
			# 이전 빌드 결과가 존재 할 경우
			if os.path.exists(oDestPath):
				os.system(f"rm -rf \"{oDestPath}\"")

		os.system(f"mv \"{oSrcPath}\" \"{oDestPath}\"")
