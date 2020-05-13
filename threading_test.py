# from multiprocessing import Process,Queue
# import os
# import time
# import random
# 写数据进程执行的代码
# def write(q):
    # print('Process to write:{}'.format(os.getpid()))
    # for value in ['A','B','C']:
        # print('Put %s to queue ...'%(value))
        # q.put(value)
        # time.sleep(random.random())
        
# 读数据进程执行的代码
# def read(q):
    # print('Process to read:{}'.format(os.getpid()))
    # while True:
    # for i in range(3):
        # value = q.get(True)
        # print('Get %s from queue'%(value))
         
# if __name__ == '__main__':
    # 父进程创建Queue,并传给各个子进程
    # q = Queue()
    # pw = Process(target=write,args=(q,))
    # pr = Process(target=read,args=(q,))
    # pw.start()

    # pw.join()
    # pr.start()
    # time.sleep(3)
    # pr.terminate()
    
import queue
import pdb
q = queue.Queue(maxsize=5)
for i in range(5):
    q.put(i)
if q.full():
    print(q.qsize())
while not q.empty():
    print(q.get())
    # pdb.set_trace()

