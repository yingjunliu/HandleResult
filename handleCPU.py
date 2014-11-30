import os
from timeClass import timeFormate

def analyseCPU(root,fileName,filedir):
	fileObject = open(os.path.join(root,fileName))
	times = fileName.split('_')
	timeFormates = timeFormate(times)
	for i in range(0,14):
		fileObject.readline()
	timeTemp = fileObject.readline()
	excTime = timeTemp[timeTemp.find(':') + 1:timeTemp.find('s')]
	excTime = excTime.replace(' ','')
	excTime = excTime.replace('\n','')
	print (timeFormates.year,timeFormates.month,timeFormates.day,timeFormates.hour,timeFormates.minute,timeFormates.second,excTime)
	fileObject = open(filedir,"a")
	fileObject.writelines(timeFormates.year+","+timeFormates.month+","+timeFormates.day+","+timeFormates.hour+","+timeFormates.minute+","+timeFormates.second+","+excTime+"\n")
	fileObject.close()