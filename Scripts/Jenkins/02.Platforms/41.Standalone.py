import os
import sys

oProjPath = sys.argv[1]
oBuildOutputPath = sys.argv[2]

oSrcPath = f"{oProjPath}/{os.path.dirname(oBuildOutputPath)}"
oDestPath = f"{oProjPath}/{oBuildOutputPath}"

os.system(f"ditto -ck --rsrc --sequesterRsrc \"{oSrcPath}\" \"{oDestPath}\"")
