import os
import sys

oProjName = sys.argv[1]

oProjPathA = f"../../../../../'{oProjName}'/Assembly-CSharp.csproj"
oProjPathB = f"../../../../../'{oProjName}'/Assembly-CSharp-Editor.csproj"
oOutputPath = f"../../../../../'{oProjName}'/Assets/01.UnityProject/Scripts/Runtime/Global/Utility/External/MessagePack/CMsgPackResolver.cs"

oConditionalSymbol = "USE_CUSTOM_PROJ_OPTS"
os.system(f"./MsgPackCompiler -i {oProjPathA},{oProjPathB} -o {oOutputPath} -c {oConditionalSymbol}")
