import os
import time

# make a new dir for the test result
rootFilePath = "/home/ubuntu/testresult/test_in_"+time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime(time.time()))
os.system("mkdir " + rootFilePath)

# test cpu
filePath = rootFilePath+"/cpuResult_in_"+time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime(time.time()))
os.system("sudo sysbench --test=cpu --cpu-max-prime=20000 run > " +filePath)

#test thread
filePath = rootFilePath+"/threadsResult_in_"+time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime(time.time()))
os.system("sudo sysbench --test=threads --num-threads=16 run > " + filePath)

#test seqence write
filePath = rootFilePath+"/seqenceWriteResult_in_"+time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime(time.time()))
os.system("sudo sysbench --test=fileio --num-threads=16 --file-total-size=4G --file-test-mode=seqwr run > " + filePath)
os.system("sudo sysbench --test=fileio --num-threads=16 --file-total-size=4G --file-test-mode=seqwr cleanup") 

#test random write
filePath = rootFilePath+"/randomWriteResult_in_"+time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime(time.time()))
os.system("sudo sysbench --test=fileio --num-threads=16 --file-total-size=4G --file-test-mode=rndwr run > " + filePath)
os.system("sudo sysbench --test=fileio --num-threads=16 --file-total-size=4G --file-test-mode=rndwr cleanup")

#test seqence read
filePath = rootFilePath+"/seqenceReadResult_in_"+time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime(time.time()))
os.system("sudo sysbench --test=fileio --num-threads=16 --file-total-size=4G --file-test-mode=seqrd prepare")
os.system("sudo sysbench --test=fileio --num-threads=16 --file-total-size=4G --file-test-mode=seqrd run > " + filePath)
os.system("sudo sysbench --test=fileio --num-threads=16 --file-total-size=4G --file-test-mode=seqrd cleanup")

#test random read
filePath = rootFilePath+"/randomReadResult_in_"+time.strftime('%Y_%m_%d_%H_%M_%S',time.localtime(time.time()))
os.system("sudo sysbench --test=fileio --num-threads=16 --file-total-size=4G --file-test-mode=rndrd prepare")
os.system("sudo sysbench --test=fileio --num-threads=16 --file-total-size=4G --file-test-mode=rndrd run > " + filePath)
os.system("sudo sysbench --test=fileio --num-threads=16 --file-total-size=4G --file-test-mode=rndrd cleanup")


