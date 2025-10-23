#Agar koi certain number se pehle kitna prime number hai wo jaan-na hoga to humlog 
#Agar Approx Jaan na hoga then we also use Prime Number Theorem
#pi(x)=x/lnx

#agar aur acha se bound nikalna
#pi(x)=integral(from 2 to x)(dt/lnt)

#Ek Riemann R Function
import math

N=10000000
prime=[True for i in range(N)]

def sieve():
    prime[0]=prime[1]=False
    for i in range(2,int(math.isqrt(N)) + 1):
        if prime[i]==True:
            for j in range(i*i,N,i):
                prime[j]=False
sieve()
primes=[]
for _ in range(N):
    if prime[_]==True:
        primes.append(_)

print(primes[10000])