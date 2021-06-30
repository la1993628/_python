"""
生成斐波那契数列的前20个数

"""
a = 1
b = 1
print(a)
print(b)
for _ in range(3,21):
	 temp = a + b
	 print(temp)
	 a = b
	 b = temp


