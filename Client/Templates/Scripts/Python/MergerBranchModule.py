import os
import sys

oProjName = sys.argv[1]
oBranchName = sys.argv[2]

os.system(f"python UpdaterModule.py \"{oProjName}\"")
os.system(f"python ExecuterCmdModule.py \"{oProjName}\" \"git merge {oBranchName}\"")
os.system(f"python ExecuterCmdModule.py \"{oProjName}\" \"git push\"")
