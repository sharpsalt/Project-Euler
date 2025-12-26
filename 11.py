import os,sys
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

L=[(input().strip().split()) for i in range(20)]
# print(L)
maxi=-10**90
for i in range(20):
    for j in range(20):
        #ek bar up mein, ek bar downm mein, ek bar left adn ek baa rright and ek baar diagnoally
        if j+3<20:
            maxi=max(maxi,int(L[i][j])*int(L[i][j+1])*int(L[i][j+2])*int(L[i][j+3]))
        if i+3<20:
            maxi=max(maxi,int(L[i][j])*int(L[i+1][j])*int(L[i+2][j])*int(L[i+3][j]))
        if i+3<20 and j+3<20:
            maxi=max(maxi,int(L[i][j])*int(L[i+1][j+1])*int(L[i+2][j+2])*int(L[i+3][j+3]))
        if i+3<20 and j-3>=0:
            maxi=max(maxi,int(L[i][j])*int(L[i+1][j-1])*int(L[i+2][j-2])*int(L[i+3][j-3]))
print(maxi)