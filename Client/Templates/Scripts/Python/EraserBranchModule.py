import os
import sys

oProjName = sys.argv[1]
oBranchName = sys.argv[2]

os.system(f"python UpdaterModule.py \"{oProjName}\"")
os.system(f"python ExecuterCmdModule.py \"{oProjName}\" \"git branch -D {oBranchName}\"")
os.system(f"python ExecuterCmdModule.py \"{oProjName}\" \"git push origin --delete {oBranchName}\"")
