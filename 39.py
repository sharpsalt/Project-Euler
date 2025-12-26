import os,sys
import math
from collections import defaultdict
from io import BytesIO,IOBase


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

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
mpp=defaultdict(int)
def ok():
    cnt=0
    #agar bahar me k se multiply kre to so many numbers are which can be made with these numbers too
    for i in range (2,1000):
        for j in range(2,i):
            if gcd(i,j)==1:
                xx=2*i*(i+j)
                if xx>1000:
                    break
                k=1
                while k*xx<=1000:
                    mpp[k*xx]+=1
                    k+=1
                # cnt+=1
                # mpp[2*(i*(i+j))]+=1 #list in ppython are mutable since it is muatble so it is unhashable
    return cnt

# print(ok(1000))
# print(mpp)

ok()
# print(mpp)
best=3
ok=120
# st=set()
for it in mpp:
    if mpp[it]>best:
        best=mpp[it]
        ok=it
print(ok)