import os
from timeClass import timeFormate

def analyseThreads(root,fileName):
	fileObject = open(os.path.join(root,fileName))
	times = fileName.split('_')
	timeFormates = timeFormate(times)
	for i in range(0,12):
		fileObject.readline()
	timeTemp = fileObject.readline()
	excTime = timeTemp[timeTemp.find(':') + 1:timeTemp.find('s')]
	excTime = excTime.replace(' ','')
	excTime = excTime.replace('\n','')
	print (timeFormates.year,timeFormates.month,timeFormates.day,timeFormates.hour,timeFormates.minute,timeFormates.second,excTime)