import os
import sys

oProjName = sys.argv[1]

os.system(f"python UpdaterModule.py \"{oProjName}\"")
os.system(f"python ExecuterCmdModule.py \"{oProjName}\" \"git gc --force\"")
