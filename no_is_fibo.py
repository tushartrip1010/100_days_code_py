import math

def check_perfect_square(m):
    final=int(math.sqrt(m))
    if pow(final,2)==m:
        return True
    return False

def check_fibo(n):
     return check_perfect_square(5*n*n + 4) or check_perfect_square(5*n*n - 4)
     
n=int(input("enter a no"))
if(check_fibo(n) == True):
    print( n," is Fibonacci number")
else:
    print( n," is not Fibnacci number")

