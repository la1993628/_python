"""
transfor F temperature to C 

Author : Ao Luo
"""

f = float(input('请输入华氏温度： '))
c = (f - 32) / 1.8
print('%.1f华氏度 = %1.f摄氏度' % (f, c))
