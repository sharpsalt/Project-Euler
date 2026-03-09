import os,sys
from io import BytesIO,IOBase
from bisect import bisect_left,bisect_right
import math
from fractions import Fraction


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
# xx=0
s=set()
x=Fraction(2)+Fraction(1,2) # bas 1+1/x krdenge to 1 step aage badh jayenge so 
for i in range(1000):
    y=Fraction(1)+Fraction(1,x)
    # print(y.numerator,y.denominator,math.log10(y.numerator),math.log10(y.denominator))
    if math.floor(math.log10(y.numerator))>math.floor(math.log10(y.denominator)):
        s.add(y)
    x=Fraction(2)+Fraction(1,x)
xx=0
for y in s:
    if math.floor(math.log10(y.numerator))>math.floor(math.log10(y.denominator)):
        xx+=1
print(xx)