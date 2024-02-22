import os
import sys

oProjName = sys.argv[1]

os.system(f"python ModuleUpdater.py \"{oProjName}\"")
os.system(f"python ModuleCmdExecuter.py \"{oProjName}\" \"git gc --force\"")
