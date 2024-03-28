import os
import sys

oProjName = sys.argv[1]

os.system(f"python ExecuterCmdModule.py \"{oProjName}\" \"git fetch -p --tags --force\"")
os.system(f"python ExecuterCmdModule.py \"{oProjName}\" \"git pull\"")
