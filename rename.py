
import os
from os import path
# files = [f for f in os.listdir(".") if path.isfile(f)]
# for fileName in files:

# 	splicedName = fileName.split('_')
# 	print splicedName[len(splicedName)-1]
# 	# print correctName
# 	os.rename(fileName,correctName)

students = next(os.walk('.'))[1]
for student in students:
	studentFiles = os.listdir(student)
	# print studentFiles
	currentFolder = os.path.join(os.getcwd(),student)
	for fileName in studentFiles:

		splicedName = fileName.split('_')
		correctName = splicedName[len(splicedName)-1]
		# print correctName

		filePath = os.path.join(currentFolder,fileName)
		correctPath = os.path.join(currentFolder,correctName)
		os.rename(filePath,correctPath)