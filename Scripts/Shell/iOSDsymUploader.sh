#/bin/bash
oProjectName=${1}
oPlistFilepath=${2}
oDsymFilepath=${3}

oSymbolUploaderPath="../../${oProjectName}/Builds/iOS/Pods/FirebaseCrashlytics/upload-symbols" -gsp ${oPlistFilepath} -p ios ${oDsymFilepath}
