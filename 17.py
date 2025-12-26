import os,sys,math
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

class Factorial:
    def __init__(self, N: int):
        N += 1
        self.f = [1] * N  # factorials
        self.g = [1] * N  # inverse factorials (will store 1/f[i] as float)
        
        for i in range(1, N):
            self.f[i] = self.f[i - 1] * i
        
        # Compute inverse factorials (no mod)
        self.g[-1] = 1 / self.f[-1]
        for i in range(N - 2, -1, -1):
            self.g[i] = self.g[i + 1] * (i + 1)
    
    def fac(self, n: int) -> int:
        """Returns n!"""
        return self.f[n]
    
    def fac_inv(self, n: int) -> float:
        """Returns 1/n! as float"""
        return self.g[n]
    
    def combi(self, n: int, m: int) -> int:
        """Returns C(n, m) = n! / (m! * (n - m)!)"""
        if m < 0 or n < 0 or n < m:
            return 0
        return int(self.f[n] * self.g[m] * self.g[n - m])
    
    def permu(self, n: int, m: int) -> int:
        """Returns P(n, m) = n! / (n - m)!"""
        if m < 0 or n < 0 or n < m:
            return 0
        return int(self.f[n] * self.g[n - m])
    
    def catalan(self, n: int) -> int:
        """Returns nth Catalan number = C(2n, n) - C(2n, n - 1)"""
        return self.combi(2 * n, n) - self.combi(2 * n, n - 1)
    
    def inv(self, n: int) -> float:
        """Returns 1/n as float using factorial relationship = (n-1)! / n!"""
        return self.f[n - 1] * self.g[n]
    
    def hockeysticksum(self, n: int, k: int) -> int:
        """Returns C(n + 1, k + 1)"""
        return self.combi(n + 1, k + 1)
    
    def pascal_sum(self, level: int, l: int, r: int) -> int:
        """
        Returns S(l, r) = C(r + level - 1, level) - C(l + level - 2, level)
        Example: like summing along Pascal's triangle diagonals
        """
        ans = self.combi(r + level - 1, level) - self.combi(l + level - 2, level)
        return ans


F=Factorial(101)
L=0
for i in range(1,101):
     for j in range(1,i+1):
        #  L.append(F.combi(i,j))
        x=F.combi(i,j)
        y=int(math.log10(x))
        # L.append()
        #1e5=1000000
        if y+1>=7:
            L+=1
print(L)