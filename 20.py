x=1
for i in range(1,101):
    x*=i
p=0
while x:
    p+=x%10
    x//=10
print(p)
