import os
import sys

oProjName = sys.argv[1]

oProjPathA = os.path.join("..", "..", "..", "..", "..", oProjName, "Assembly-CSharp.csproj")
oProjPathB = os.path.join("..", "..", "..", "..", "..", oProjName, "Assembly-CSharp-Editor.csproj")
oOutputPath = os.path.join("..", "..", "..", "..", "..", oProjName, "Assets", "01.UnityProject", "Scripts", "Runtime", "Global", "Utility", "External", "MessagePack", "CMsgPackResolver.cs")

oDefineSymbol = "MSG_PACK_ENABLE"
oConditionalSymbol = "USE_CUSTOM_PROJ_OPT"

os.system(f"./MsgPackCompiler -i {oProjPathA},{oProjPathB} -o {oOutputPath} -c {oConditionalSymbol} -ms {oDefineSymbol}")
