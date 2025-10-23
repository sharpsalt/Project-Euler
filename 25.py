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

# INF = 10**9+7
n=2

class Matrix:
    def __init__(self):
        self.a = [[0] * n for _ in range(n)]

    def __mul__(self, other):
        product = Matrix()
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    product.a[i][k] = (product.a[i][k] + self.a[i][j] * other.a[j][k])
        return product


def expo_power(a: Matrix, k: int) -> Matrix:
    product = Matrix()
    # make identity matrix
    for i in range(n):
        product.a[i][i] = 1
    while k > 0:
        if k & 1:
            product = product * a
        a = a * a
        k //= 2
    return product

A=Matrix()
A.a=[[1,1],[1,0]]
for i in range(1,10000):
    result=expo_power(A,i)
    if int(math.log10(result.a[0][0]+result.a[0][1]))+1==1000:
        print(i)
        sys.exit()
