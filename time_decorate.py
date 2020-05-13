import time
import pdb
def print_fun_time(fun):
	def show_fun_time(*args,**kwargs):
		start_time=time.time()
		fun()
		stop_time=time.time()
		#pdb.set_trace()
		print('本函数花费时间%f秒'%(stop_time-start_time))
	return show_fun_time

if __name__ == '__main__':
	print_fun_time(func)
