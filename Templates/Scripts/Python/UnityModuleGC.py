import os
import sys

oProjName = sys.argv[1]

os.system(f"python3 UnityModuleUpdater.py \"{oProjName}\"")
os.system(f"python3 UnityModuleCmdExecuter.py \"{oProjName}\" \"git gc --force\"")
