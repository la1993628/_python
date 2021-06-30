"""
输出100以内所有的素数
"""

n = 1
for i in range(2,100):
	flag = True
	for j in range(2,i):
		if( i % j == 0 ):
			flag = False
	if( flag ):
		print(i)
