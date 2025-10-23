x=1

def gcd(a,b):
    if b==0:
        return a
    else:
       return gcd(b,a%b)
    
def lcm(a,b):
    return a*b//gcd(a,b)

#gcd*lcm=a*b
#so 

for i in range(1,21):
    x=lcm(x,i)
    # print(i)
print(x)

