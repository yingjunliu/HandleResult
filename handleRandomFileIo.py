import os
from timeClass import timeFormate

def analyseRandomFileIo(root,fileName,filedir):
	fileObject = open(os.path.join(root,fileName))
	times = fileName.split('_')
	timeFormates = timeFormate(times)
	for i in range(0,19):
		fileObject.readline()
	temp = fileObject.readline()
	bandWith = temp[temp.find('(') + 1:temp.find('Mb/s')]
	temp = fileObject.readline()
	request = temp[1:temp.find("Request")]
	request = request.replace(' ','')
	print (timeFormates.year,timeFormates.month,timeFormates.day,timeFormates.hour,timeFormates.minute,timeFormates.second,bandWith,request)
	fileObject = open(filedir,"a")
	fileObject.writelines(timeFormates.year+","+timeFormates.month+","+timeFormates.day+","+timeFormates.hour+","+timeFormates.minute+","+timeFormates.second+","+bandWith+","+request+"\n")
	fileObject.close()