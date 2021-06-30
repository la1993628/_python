"""
打印如下所示的三角形图案
"""
row = int(input('请输入行数：'))
for i in range(row):
	for _ in range(i+1):
		print('*',end='')