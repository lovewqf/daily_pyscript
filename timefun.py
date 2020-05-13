import time
import pdb
def timeFun():
	start_time = time.time()
	time.sleep(2)
	end_time = time.time()
	pdb.set_trace()
	
if __name__ == '__main__':
	timeFun()