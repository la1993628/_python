"""

input the radius of a circle to calculate its circumference and area

"""

r = float(input('输入圆的半径: '))
c = 2 * 3.1416 * r
A = 3.1416 * (r**2)

print('半径为%.1f的圆的周长和面积分别为:%.2f,%.2f' % (r , c ,A)) 