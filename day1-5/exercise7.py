"""
找出所有的水仙花数
"""

for n in range(100,1000):
	low = n % 10
	mid = n // 10 % 10
	high = n // 100
	if n == low **3 + mid **3 + high ** 3:
		print(n)