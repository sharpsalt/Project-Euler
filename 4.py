#from 3 digit means that ki 100 to 999
#10000 to 
#10^4 to 1e8-1

def ispalindrome(s):
    return s==s[::-1]
N=10**6-1
# print(
maxi=-1**9
for i in range(1000,100,-1):
    for j in range(1000,100,-1):
        x=i*j
        if ispalindrome(str(x)):
            maxi=max(maxi,x)
print(maxi)