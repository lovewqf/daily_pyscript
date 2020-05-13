import pandas as pd
import numpy as np
import pdb
class Test(object):
	def __init__(self):
		self.name = 'lcyin'
		self.age = 24
	def read_Excel(self,path):
		df_dict = pd.read_excel(path,sheet_name=None)
		for sheet_name,df in df_dict.items():
			print('工作蒲的名字为:%s'% sheet_name)
			print(df)

	def write_Excel(self):
		arr1 = np.array([[1,2,3],[4,5,6]])
		arr2 = np.array([[11,22,33],[44,55,66]])
		writer = pd.ExcelWriter(r'C:\\Users\\yin\\Desktop\\qwer_asdf.xlsx')
		df1 = pd.DataFrame(arr1).to_excel(writer,sheet_name='表1',index=['q','w','e'])
		df2 = pd.DataFrame(arr2).to_excel(writer,sheet_name='表2')
		writer.save()
		writer.close()
		print('数据写入成功')
		pass
if __name__ == '__main__':
	path = r'C:\\Users\\yin\\Desktop\\qwer.xlsx'
	#Test.read_Excel(path)
	t = Test()
	t.read_Excel(path)
	t.write_Excel()
	print(t.name)
	print(t.age)