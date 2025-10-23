#Since we know the property of Pythagorean Tripletes that Euclid Formula is one of the way to represent it 
#so anyhow 
#a=m2-n2
#b=2mn
#c=m2+n2
#where m and n are coprime and both are not odd

#Since to get a+b+c=1000 mtlb =2m2+2mn=2m(m+n)

import sys

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

for m in range(1, 1000):
    for n in range(1, m):
        if ((m % 2 == 0 and n % 2 == 1) or (m % 2 == 1 and n % 2 == 0)) and gcd(m, n) == 1:
            p0 = 2 * m * (m + n) 
            if 1000 % p0 == 0:
                k = 1000 // p0
                a = k * (m * m - n * n)
                b = k * (2 * m * n)
                c = k * (m * m + n * n)
                print(a*b*c)
                sys.exit()

