dp=[0 for i in range(10000005)]
dp[0]=1
dp[1]=2
# print(dp)
for i in range(2,10000005,1):
    dp[i]=dp[i-1]+dp[i-2]
    if dp[i]>4000000:
        break

x=sum(it for it in dp if it<=4000000 and it%2==0)
print(x)