import os
import sys

oProjName = sys.argv[1]
oCommitMsg = sys.argv[2]
oBranchName = sys.argv[3]

oCommitCmd = f"git commit -m \"{oCommitMsg}\""

os.system(f"python3 UnityModuleCmdExecuter.py \"{oProjName}\" \"git add .\"")
os.system(f"python3 UnityModuleCmdExecuter.py \"{oProjName}\" \"{oCommitCmd}\"")

# 브랜치 이름이 유효 할 경우
if len(oBranchName) >= 1:
	os.system(f"python3 UnityModuleCmdExecuter.py \"{oProjName}\" \"git push origin -u {oBranchName}\"")
else:
	os.system(f"python3 UnityModuleCmdExecuter.py \"{oProjName}\" \"git push\"")
