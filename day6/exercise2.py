def add(*args):
	total = 0
	for val in args:
		total += val
	return total

#在调用add函数时可以传入0个或多个参数
print(add())
print(add(1))
print(add(1,2))
print(add(1,2,3))
print(add(1,3,5,7,9))
