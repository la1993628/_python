"""
输入年份判断是不是闰年

"""

y = int(input('输入年份：'))
if( y%4 == 0 and y%100 != 0 or y % 400 == 0):
	print( True)
else:
	print( False )
	