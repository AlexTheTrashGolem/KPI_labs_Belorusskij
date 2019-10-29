import math
<<<<<<< HEAD
x=float(input())
=======
x = float(input())
>>>>>>> 61192926e40c3e7bb01fb243c9e8487d6248d5a2
if x>4 or x<0:
    raise Exception('x has to be in [0;4]')
counter=1
s=0
<<<<<<< HEAD
s_current=1
while s_current>=0.000001 or s_current<=-0.000001:
    s+=s_current
    s_current=(-1)**counter*x**(2*counter)/math.factorial(2*counter)
=======
s_current=x**0
while s_current>=0.000001 or s_current<=-0.000001:
    s+=s_current
    s_current=s_current*(-1)*x**2/(2*counter-1)
>>>>>>> 61192926e40c3e7bb01fb243c9e8487d6248d5a2
    counter+=1
s=(s//0.001)/1000
print(s)
