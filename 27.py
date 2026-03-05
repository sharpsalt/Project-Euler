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

v=[]
prime=[True for i in range(100002)]
prime[0]=prime[1]=False
for i in range(2,len(prime)):
    if prime[i]==True:
        for j in range(2*i,len(prime),i):
            prime[j]=False

for i in range(1001):
    if prime[i]==True:
        v.append(i)
maxi=-10000000
val=-100000000
for i in v:
    for j in range(-1000,1001):
        n=1
        def value(n,i,j):
            return n**2 + j*n + i
        while prime[value(n,i,j)]:
            n+=1
        if n>maxi:
            maxi=n
            val=i*j
print(val)

#The concept which we know that
# n^2+n+41 it is very famous prime generating function like 
#It is alsoc alled as Euler's prime generating function

#For every integer n=0,1,2...39 the value of the equation is prime
#like 40 consecutive prime number milta hai 

#wahi uske jagah n^2-n+41 is nothing but just same Euler's polynomial shifted by 1
#n^2-n+41=(n-1)^2 + (n-1) + 41


#so is question me diya hua formula n^2-79n+1601 is nothing more 
#(n-40)^2+(n-40)+41 //basicaly it is shifted by 40 
#thats all the forty primes of n^2+n+41 are met twice that's why 80 primes are found
#but only 40 are different ones

#take (n-p)^2+(n-p)+41 , working out on this formula gives:
#n^2-(2p-1)n+p^2-p+41 
#ab question me likha tha ki |a|<1000 and |b|<1000
#so |2p-1|<1000 and |p^2-p+41|<1000
#isme se second condition gives p belongs to [-30,31]
#so the number are -(2*31-1)=-61 and 31^2-31+41=971


