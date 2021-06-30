"""
输入一个正整数判断是不是素数。
提示：素数指的是只能被1和自身整除的大于1的整数

"""
from math import sqrt
n = int(input('输入一个正整数:'))
if( n <= 1):
	print('不是素数')
for x in range(2,sqrt(n)+1):
	if( n % x == 0):
		print('不是素数')
		break;
else:
	print('是素数')