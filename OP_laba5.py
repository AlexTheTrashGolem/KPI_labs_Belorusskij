from math import sqrt

def if_prime(x):
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0 and x != i:
            return False
    return True

n = int(input("n = "))
for x in range(2, int(n / 2) + 1):
    if n % x == 0 and if_prime(x):
        print (x)
