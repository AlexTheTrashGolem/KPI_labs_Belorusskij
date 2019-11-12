import math
x = float(input())
if x > 4 or x < 0:
    raise Exception('x has to be in [0;4]')
counter=1
s=0
s_current=x**0
while s_current>=0.000001 or s_current<=-0.000001:
    s += s_current
    s_current = s_current * (-1) * x ** 2 / (2 * counter-1)
    counter += 1
s=(s // 0.001) / 1000
print(s)
