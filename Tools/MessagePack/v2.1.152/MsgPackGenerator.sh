#!/bin/bash
g_oProjectName=${1}

g_oPath="$(cd "$(dirname "${0}")" && pwd -P)"
g_oProjectPathA="${g_oPath}/../../../../../${g_oProjectName}/Assembly-CSharp.csproj"
g_oProjectPathB="${g_oPath}/../../../../../${g_oProjectName}/Assembly-CSharp-Editor.csproj"
g_oDefineSymbol="MESSAGE_PACK_ENABLE"
g_oConditionalSymbol="USE_CUSTOM_PROJ_OPT"

${g_oPath}/MsgPackCompiler -i ${g_oProjectPathA},${g_oProjectPathB} -o "${g_oPath}/../../../../../${g_oProjectName}/Assets/01.UnityProject/Scripts/Runtime/Global/Utility/External/MessagePack/CMsgPackResolver.cs" -c ${g_oConditionalSymbol} -ms ${g_oDefineSymbol}
