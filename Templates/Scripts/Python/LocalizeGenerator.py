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

oCommonValueList = [
	"ID", "Replace", "Description"
]

# 헤더 정보를 설정한다 {
oHeaderList = []
oLanguageList = []

for oCell in oLocalizeSheet[nHeaderNumber]:
	# 값이 유효 할 경우
	if oCell.value:
		oHeaderList.append(oCell.value)

		# 공용 값 일 경우
		if not oCell.value in oCommonValueList:
			oLanguageList.append(oCell.value)

# 헤더 정보를 설정한다 }

# 값을 설정한다 {
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
# 값을 설정한다 }

# 지역화를 설정한다 {
oCommonLocalizeInfo = []
oLocalizeInfoListContainer = {}

for i, oValueList in enumerate(oValueListContainer):
	for j, oValue in enumerate(oValueList):
		# 지역화 값이 아닐 경우
		if j < int(nLocalizeStartIndex):
			oCommonLocalizeInfo.append(oValue)
		else:
			oKey = oHeaderList[j]

			# 지역화 정보 리스트가 없을 경우
			if not oKey in oLocalizeInfoListContainer:
				oLocalizeInfoListContainer[oKey] = []

			oLocalizeInfo = []

			for k, oCommonValue in enumerate(oCommonLocalizeInfo):
				oLocalizeInfo.append(oCommonValue)

			# 언어 헤더 일 경우
			if i <= 0 and oValue in oLanguageList:
				oLocalizeInfo.append("String")
			else:
				# , 문자가 존재 할 경우
				if "," in oValue:
					oLocalizeInfo.append("\"" + oValue + "\"")
				else:
					oLocalizeInfo.append(oValue)

			oLocalizeInfoListContainer[oKey].append(oLocalizeInfo)

	oCommonLocalizeInfo = []
# 지역화를 설정한다 }

# 지역화 파일을 생성한다 {
for oKey, oLocalizeInfoList in oLocalizeInfoListContainer.items():
	# 디렉토리가 없을 경우
	if not os.path.isdir(oOutputPath):
		os.makedirs(oOutputPath)

	oFilepath = f"{oOutputPath}/{oOutputFilename}_{oKey}.csv"
	oWStream = open(oFilepath, "w")

	for i, oLocalizeInfo in enumerate(oLocalizeInfoList):
		for j, oValue in enumerate(oLocalizeInfo):
			oWStream.write(str(oValue))

			if j < len(oLocalizeInfo) - 1:
				oWStream.write(",")
			elif i < len(oLocalizeInfoList) - 1:
				oWStream.write("\n")

	oWStream.close()
# 지역화 파일을 생성한다 }
