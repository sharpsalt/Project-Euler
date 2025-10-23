s=input()

def calc(ss):
    x=1
    for i in range(len(ss)):
        x*=int(ss[i])
    return x

maxi=0
for i in range(0,988):
    sss=s[i:i+13]
    maxi=max(maxi,calc(sss))
print(maxi)