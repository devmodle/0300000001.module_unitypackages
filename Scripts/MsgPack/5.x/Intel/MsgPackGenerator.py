import os
import sys

oProjPath = f"../../../../../../\"{sys.argv[1]}\""
oOutputPath = f"../../../../../../\"{sys.argv[1]}\"/Assets/02.SubUnityProject/Scripts/Runtime/Global/Utility/External/MessagePack/CMsgPackResolver.cs"
oConditionalSymbols = f"EXTRA_SCRIPT_MODULE_ENABLE,{sys.argv[2]}"

os.system(f"/usr/local/share/dotnet/dotnet tool restore")
os.system(f"/usr/local/share/dotnet/dotnet mpc -i \"{oProjPath}\" -o \"{oOutputPath}\" -c \"{oConditionalSymbols}\" -ms \"EXTRA_SCRIPT_MODULE_ENABLE\"")
