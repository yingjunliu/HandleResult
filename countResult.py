import os
import os.path
import shutil
from handleCPU import analyseCPU
from handleThreads import analyseThreads
from handleRandomFileIo import analyseRandomFileIo
from handleSeqenceFileIo import analyseSeqenceFileIo
rootdir = "E:\\testResult"
resultdir = ""

def directoryScan(rootdir):
	global resultdir
	if not os.path.isdir(resultdir):
		os.makedirs(resultdir)
	for root, dirs, files in os.walk(rootdir):
		# for dir in dirs:
			# print (dir)
			# directoryScan(os.path.join(root,dir))
		for file in files:
			# print (file.split('_'))
			filenames = file.split('_')
			if filenames[0].find("cpu") >= 0:
				cpuresult = os.path.join(resultdir,"cpuresult.csv")
				analyseCPU(root,file,cpuresult)
			elif filenames[0].find("thread") >= 0:
				analyseThreads(root,file)
			elif filenames[0].find("random") >= 0:
				analyseRandomFileIo(root,file)
			elif filenames[0].find("seqence") >= 0:
				analyseSeqenceFileIo(root,file)

if __name__ == "__main__" :
	resultdir = os.path.join(rootdir,"testresult")
	if os.path.isdir(resultdir):
		# os.removedirs(resultdir)
		shutil.rmtree(resultdir) #删除
	directoryScan(rootdir)