import os,sys
from io import BytesIO,IOBase
from collections import defaultdict
import math


#Copied from https://codeforces.com/blog/entry/71884
BUFSIZ=8192
class FastIO(IOBase):
    newlines=0
    def __init__(self,file):
        self._fd=file.fileno()
        self.buffer=BytesIO()
        self.writable="n"in file.mode or "r" not in file.mode
        self.write=self.buffer.write if self.writable else None
    def read(self):
        while True:
            b=os.read(self._fd,max(os.fstat(self._fd).st_size,BUFSIZ))
            if not b:
                break
            ptr=self.buffer.tell()
            self.buffer.seek(0,2),self.buffer.write(b),self.buffer.seek(ptr)
        self.newlines=0
        return self.buffer.read()
    def readline(self):
        while self.newlines==0:
            b=os.read(self._fd,max(os.fstat(self._fd).st_size, BUFSIZ))
            self.newlines=b.count(b"\n")+(not b)
            ptr=self.buffer.tell()
            self.buffer.seek(0, 2),self.buffer.write(b),self.buffer.seek(ptr)
        self.newlines-=1
        return self.buffer.readline()
    def flush(self):
        if self.writable:
            os.write(self._fd,self.buffer.getvalue())
            self.buffer.truncate(0),self.buffer.seek(0)

class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer=FastIO(file)
        self.flush=self.buffer.flush
        self.writable=self.buffer.writable
        self.write=lambda s:self.buffer.write(s.encode("ascii"))
        self.read=lambda:self.buffer.read().decode("ascii")
        self.readline=lambda:self.buffer.readline().decode("ascii")

#if os.path.exists("input.txt"):
#    sys.stdin=open("input.txt", "r")
#    sys.stdout=open("output.txt", "w")
# sys.stdin,sys.stdout = IOWrapper(sys.stdin),IOWrapper(sys.stdout)
if sys.version_info[0]<3:
    sys.stdin,sys.stdout=FastIO(sys.stdin),FastIO(sys.stdout)
else:
    sys.stdin,sys.stdout=IOWrapper(sys.stdin),IOWrapper(sys.stdout)
input=lambda:sys.stdin.readline().rstrip("\r\n")

#bootstarp-pyboot

# def ispandigital(a,b,c):
#     mp=defaultdict(int)
#     for _ in range(1,10):
#         mp[_]+=1
#     s1=str(a)
#     s2=str(b)
#     s3=str(c)
#     mp1=defaultdict(int)
#     for i in range(len(s1)):
#         mp1[int(s1[i])]+=1
#     for i in range(len(s2)):
#         mp1[int(s2[i])]+=1
#     for i in range(len(s3)):
#         mp1[int(s3[i])]+=1
#     # print(mp1)
#     for i in mp1:
#         if i not in mp:
#             return False
    
#     for i in mp1:
#         if mp[i]!=mp1[i]:
#             return False
#     return True

def ispandigital(a, b, c):
    s=str(a)+str(b)+str(c)
    if len(s)!=9:
        return False
    return set(s)==set("123456789")

ans=[]
def check(a,b):
    c=a*b
    return len(str(a))+len(str(b))+len(str(c))==9

for i in range(1,11):
    x=10**i#10 and 99
    y=10**(i+1)
    y-=1
    for j in range(1,11):
        x1=10**j
        y1=10**(i+1)
        y1-=1
        
        #ab check krenge ki iska sum total 9 jaabhi paraha hai ya nahi 
        if check(x,x1):
            ans.append([x,x1])
        if check(x,y1):
            ans.append([x,y1])
        if check(y,x1):
            ans.append([y,x1])
        if check(y,y1):
            ans.append([y,y1])
# print(ans)
def find_pandigital_products():
    products=set()
    for i in range(1,10):
        for j in range(1000,10000):
            product=i*j
            if ispandigital(i,j,product):
                products.add(product)
    
    for i in range(10,100):
        for j in range(100,1000):
            product=i*j
            if ispandigital(i,j,product):
                products.add(product)
    
    return products
pandigital_products=find_pandigital_products()
print("Pandigital identities found:")
for prod in sorted(pandigital_products):
    print(f"Product: {prod}")

print(f"\nSum of all pandigital products: {sum(pandigital_products)}")