import sys
num=sys.stdin.read().strip().split()
# print(num)
x=0
for i in range(len(num)):
    x+=int(num[i])
print(x)