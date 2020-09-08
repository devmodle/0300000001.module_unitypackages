import os
import sys

from openpyxl import load_workbook

oExcelFilepath = sys.argv[1]
oOutputPath = sys.argv[2]
oLocalizeSheetname = sys.argv[3]
oOutputFilename = sys.argv[4]
nHeaderNumber = sys.argv[5]
nLocalizeStartIndex = sys.argv[6]

oWorkspace = load_workbook(oExcelFilepath, data_only = True)
oLocalizeSheet = oWorkspace[oLocalizeSheetname]

# 헤더 정보 리스트를 설정한다 {
oHeaderList = []

for oCell in oLocalizeSheet[nHeaderNumber]:
	# 값이 유효 할 경우
	if oCell.value:
		oHeaderList.append(oCell.value)
# 헤더 정보 리스트를 설정한다 }

# 값 리스트를 설정한다 {
nIndex = 0
oValueListContainer = []

for oRow in oLocalizeSheet.rows:
	if nIndex >= int(nHeaderNumber) - 1:
		oValuelList = []

		for oCell in oRow:
			# 값이 유효 할 경우
			if oCell.value:
				oValuelList.append(oCell.value)
		
		oValueListContainer.append(oValuelList)

	nIndex += 1
# 값 리스트를 설정한다 }

# 지역화 리스트를 설정한다 {
oCommonLocalizeInfo = []
oLocalizeInfoListContainer = {}

for i, oValueList in enumerate(oValueListContainer):
	for j, oValue in enumerate(oValueList):
		# 지역화 값이 아닐 경우
		if j < int(nLocalizeStartIndex):
			oCommonLocalizeInfo.append({
				"Key": oHeaderList[j], "Value": oValue
			})
		else:
			oKey = oHeaderList[j]

			# 지역화 정보 리스트가 없을 경우
			if not oKey in oLocalizeInfoListContainer:
				oLocalizeInfoListContainer[oKey] = []

			oLocalizeInfo = []

			for k, oCommonValue in enumerate(oCommonLocalizeInfo):
				oLocalizeInfo.append({
					"Key": oCommonValue["Key"], "Value": oCommonValue["Value"]
				})

			# , 문자가 존재 할 경우
			if "," in oValue:
				oLocalizeInfo.append({
					"Key": "String", "Value": "\"" + oValue + "\""
				})
			else:
				oLocalizeInfo.append({
					"Key": "String", "Value": oValue
				})

			oLocalizeInfoListContainer[oKey].append(oLocalizeInfo)

	oCommonLocalizeInfo = []
# 지역화 리스트를 설정한다 }

# 지역화 파일을 생성한다 {
for oKey, oLocalizeInfoList in oLocalizeInfoListContainer.items():
	# 디렉토리가 없을 경우
	if not os.path.isdir(oOutputPath):
		os.makedirs(oOutputPath)

	oFilepath = os.path.join(oOutputPath, oOutputFilename + "_" + oKey + ".csv")
	oWStream = open(oFilepath, "w")

	for i, oLocalizeInfo in enumerate(oLocalizeInfoList):
		for j, oLocalizeValue in enumerate(oLocalizeInfo):
			oWStream.write(str(oLocalizeValue["Value"]))

			if j < len(oLocalizeInfo) - 1:
				oWStream.write(",")
			elif i < len(oLocalizeInfoList) - 1:
				oWStream.write("\n")

	oWStream.close()
# 지역화 파일을 생성한다 }
