import os
import sys

oParams = {
	"ProjPath": sys.argv[1],
	"BuildOutputPath": sys.argv[2],
	"Platform": sys.argv[3],
	"ProjPlatform": sys.argv[4],
	"BuildFunc": sys.argv[5]
}

oSrcPath = f"{oParams["ProjPath"]}/{os.path.dirname(oParams["BuildOutputPath"])}"
oDestPath = f"{oParams["ProjPath"]}/{oParams["BuildOutputPath"]}"

os.system(f"ditto -ck --rsrc --sequesterRsrc \"{oSrcPath}\" \"{oDestPath}\"")
