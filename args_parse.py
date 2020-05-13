import os,sys
import pdb
def args_Parse(*args,**kwargs):
	print(args)
	for i in list(args)[0]:	
		print(i)
		pdb.set_trace()

	for k,v in kwargs.items():
		print(k,v)
if __name__ == '__main__':
	path = sys.argv[0]
	a = sys.argv[1]
	b = sys.argv[2]
	args_Parse(sys.argv,name='lcyin')