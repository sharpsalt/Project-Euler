import os,sys
import math
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

if os.path.exists("input.txt"):
    sys.stdin=open("input.txt", "r")
    sys.stdout=open("output.txt", "w")
# sys.stdin,sys.stdout = IOWrapper(sys.stdin),IOWrapper(sys.stdout)
if sys.version_info[0]<3:
    sys.stdin,sys.stdout=FastIO(sys.stdin),FastIO(sys.stdout)
else:
    sys.stdin,sys.stdout=IOWrapper(sys.stdin),IOWrapper(sys.stdout)
input=lambda:sys.stdin.readline().rstrip("\r\n")

#bootstarp-pyboot

#one thing whcih i can do is ki pehle saare divisble wale ko lelenge and ek map banle like whatever number have 500 or 500+ divisors and check if it is traingale nmber or not 
#i*(i+1)/2=x=>x*2=i*(i+1) i can ok hojayega  but precomputing doesn't work here so like every triangle number to the next one is difference of its index


def count_divisors(n):
    cnt=0
    sq=int(math.isqrt(n))
    for i in range(1,sq+1):
        if n%i==0:
            cnt+=2
    if sq*sq==n:
        cnt-=1
    return cnt

n=1
tri=1
while True:
    divs=count_divisors(tri)
    if divs>=500:
        print(tri)
        break
    n+=1
    tri+=n
#i am really fool i can solve this problem with more easy eay too.... no ;.//