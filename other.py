import sys
import math
import cmath


msg = int(123)
pe = int(123) #Pei's
n = int(123) #Pei's

p = int(123)
q = int(123)

newn = int(p*q)
phi=int((p-1)*(q-1))
e = int(70001)

reply = int(123)


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


d = int(-123)
d = d+phi

#print modular(reply,d,newn)
print modular(msg,pe,n)

#print newn

#result = xgcd(e, phi)
#for i in result:
#    print i

#print gcd(phi,e)
