import os
import sys

oProjPath = f"../../../../\"{sys.argv[1]}\""
oOutputPath = f"../../../../\"{sys.argv[1]}\"/Assets/03.SubUnityProject/Scripts/Runtime/Global/Utility/External/MessagePack/CMsgPackResolver.cs"
oConditionalSymbols = f"MSG_PACK_ENABLE,EXTRA_SCRIPT_MODULE_ENABLE,NEWTON_SOFT_JSON_MODULE_ENABLE,{sys.argv[2]}"

os.system(f"dotnet tool restore")
os.system(f"dotnet mpc -i \"{oProjPath}\" -o \"{oOutputPath}\" -c \"{oConditionalSymbols}\" -ms \"MSG_PACK_ENABLE&&EXTRA_SCRIPT_MODULE_ENABLE&&NEWTON_SOFT_JSON_MODULE_ENABLE\"")
