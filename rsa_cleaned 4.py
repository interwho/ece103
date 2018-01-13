import sys
import math
import cmath


msg = int("038")
pe = int(123) #Pei's
n = int(123) #Pei's

a = int(123)
b = int(123)

p=int(a-1)
q=int(b-1)

phi=int(123)

e = int(70001)

def xgcd(a,b):
    prevx, x = 1, 0; prevy, y = 0, 1
    while b:
        q = a/b
        x, prevx = prevx - q*x, x
        y, prevy = prevy - q*y, y
        a, b = b, a % b
    return a, prevx, prevy

def modular(base, exp, mod):
    x = 1
    power = base % mod

    i = 0
    while i < (sys.getsizeof(int) * 8):
        least_sig_bit = 0x00000001 & (exp >> i)
        if (least_sig_bit):
            x = (x * power) % mod
        power = (power * power) % mod
        i = i+1

    return x

#result = xgcd(on,e)
#for i in result:
#    print i
    
print xgcd(e,phi)
