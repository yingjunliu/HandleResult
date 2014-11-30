import os
import os.path
import shutil
from handleCPU import analyseCPU
from handleThreads import analyseThreads
from handleRandomFileIo import analyseRandomFileIo
from handleSeqenceFileIo import analyseSeqenceFileIo
rootdir = r"E:\云服务器运行数据\testresult_amazon"
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
				cpuresult = os.path.join(resultdir,"cpuResult.csv")
				analyseCPU(root,file,cpuresult)
			elif filenames[0].find("thread") >= 0:
				threadresult = os.path.join(resultdir,"threadResult.csv")
				analyseThreads(root,file,threadresult)
			elif filenames[0].find("random") >= 0:
				randomresult = ""
				if filenames[0].find("Read") >= 0:
					randomresult = os.path.join(resultdir,"randomReadResult.csv")
				elif filenames[0].find("Write") >= 0:
					randomresult = os.path.join(resultdir,"randomWriteResult.csv");
				analyseRandomFileIo(root,file,randomresult)
			elif filenames[0].find("seqence") >= 0:
				seqenceresult = ""
				if filenames[0].find("Read") >= 0:
					seqenceresult = os.path.join(resultdir,"seqenceReadResult.csv")
				elif filenames[0].find("Write") >= 0:
					seqenceresult = os.path.join(resultdir,"seqenceWriteResult.csv");
				analyseSeqenceFileIo(root,file,seqenceresult)

if __name__ == "__main__" :
	resultdir = os.path.join(rootdir,"testFinalResult")
	if os.path.isdir(resultdir):
		# os.removedirs(resultdir)
		shutil.rmtree(resultdir) #删除
	directoryScan(rootdir)