from math import sqrt

a = int(input("Введіть A"))
b = int(input("Введіть B"))
c = int(input("Введіть C"))
d = int(input("Введіть D"))

def func_1 ( x , y ):
    return ( x**2 - y**2 )

def func_2 ( x , y , z ):
    return ( ( x + y ) / 4 / z / x )

answer = (func_1 ( a , b ) + func_1 ( c + d ) ) / sqrt ( func_2 ( a , b , c ) )
    + ( c - func_2( a , b , c ) + 1 ) / (func_1( b , c ) + func_1( a , b) ) *
    ( 1 + sqrt ( func_2( a, b, c ) ) / (func_1 ( b , c ) - func_1 ( a , c ) ) )

print(answer)
