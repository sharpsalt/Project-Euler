#prime factor mera 2 , 3 , ya 5, 7 ,11,13 , 17,19, 23,
#5 tak ok hai phir 
#7 phir 11 se 11,13 phir aisehikrkte krte hai soon

n=int(input())
N=10**7

#ab hum absically sieve chala denge 
prime=[True for i in range((N+1))]
prime[0]=False
prime[1]=False
primes=[]

for i in range(2,int(N ** 0.5) + 1):
    if prime[i]:
        for j in range(i*i,N+1,i):
            prime[j]=False

for i in range(2, N + 1):
    if prime[i]:
        primes.append(i)
ans=[]
# print(primes)
for _ in range(len(primes)):
    if n%primes[_]==0:
        ans.append(primes[_])
# print(ans)
print(ans[-1])