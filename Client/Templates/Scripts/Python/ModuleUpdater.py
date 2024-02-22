import os
import sys

oProjName = sys.argv[1]

os.system(f"python ModuleCmdExecuter.py \"{oProjName}\" \"git fetch -p --tags --force\"")
os.system(f"python ModuleCmdExecuter.py \"{oProjName}\" \"git pull\"")
