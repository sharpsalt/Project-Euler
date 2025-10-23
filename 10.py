import math
N=2000001
primes=[True for i in range(N)]

def sieve():
    primes[0]=primes[1]=False
    for i in range(2,int(math.sqrt(N))+1):
        if primes[i]==True:
            for j in range(i*i,N,i):
                primes[j]=False

prime=[]
sieve()
for _ in range(N):
    if primes[_]:
        prime.append(_)
# print(prime)
x=sum(prime)
print(x)