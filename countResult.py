import os
import os.path
from handleCPU import analyseCPU
from handleThreads import analyseThreads
from handleRandomFileIo import analyseRandomFileIo
from handleSeqenceFileIo import analyseSeqenceFileIo
rootdir = "E:\\testResult"

def directoryScan(rootdir):
	for root, dirs, files in os.walk(rootdir):
		# for dir in dirs:
			# print (dir)
			# directoryScan(os.path.join(root,dir))
		for file in files:
			# print (file.split('_'))
			filenames = file.split('_')
			if filenames[0].find("cpu") >= 0:
				analyseCPU(root,file)
			elif filenames[0].find("thread") >= 0:
				analyseThreads(root,file)
			elif filenames[0].find("random") >= 0:
				analyseRandomFileIo(root,file)
			elif filenames[0].find("seqence") >= 0:
				analyseSeqenceFileIo(root,file)

if __name__ == "__main__" :
	directoryScan(rootdir)