import os
import sys

oProjName = sys.argv[1]

oProjPathA = f"../../../../../'{oProjName}'/Assembly-CSharp.csproj"
oProjPathB = f"../../../../../'{oProjName}'/Assembly-CSharp-Editor.csproj"
oOutputPath = f"../../../../../'{oProjName}'/Assets/01.UnityProject/Scripts/Runtime/00.AutoCreate/Global/Utility/External/MessagePack/CMsgPackResolver.cs"

oConditionalSymbol = "MSG_PACK_ENABLE,USE_CUSTOM_PROJ_OPTS"
os.system(f"./MsgPackCompiler -i {oProjPathA},{oProjPathB} -o {oOutputPath} -c {oConditionalSymbol} -ms MSG_PACK_ENABLE")
