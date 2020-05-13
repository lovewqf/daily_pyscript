import time,sys
from tqdm import tqdm
from time import sleep
def process_Shape():
	print('正在下载...')
	for i in range(11):
		if i!=10:
			sys.stdout.write('==')
		else:
			sys.stdout.write('=='+str(i*10)+'%')
		sys.stdout.flush()
		time.sleep(0.5)
	print('\n下载成功')


def shape():
	for i in tqdm(range(10)):
		sleep(0.5)
	



if __name__ == '__main__':
	process_Shape()
	shape()