import os,sys
from io import BytesIO,IOBase
import math
from collections import defaultdict,OrderedDict


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

def sieve(N: int, Q: int = 17, L: int = 1 << 15):
    rs = [1, 7, 11, 13, 17, 19, 23, 29]

    class P:
        def __init__(self, p: int):
            self.p = p
            self.pos = [0] * 8

    def approx_prime_count(N: int) -> int:
        if N > 60184:
            return int(N / (math.log(N) - 1.1))
        else:
            return int(max(1.0, N / (math.log(N) - 1.11)) + 1)

    v = int(math.isqrt(N))
    vv = int(math.isqrt(v))
    isp = [True] * (v + 1)
    for i in range(2, vv + 1):
        if isp[i]:
            for j in range(i * i, v + 1, i):
                isp[j] = False

    rsize = approx_prime_count(N + 30)
    primes = [2, 3, 5]
    psize = 3

    sprimes = []
    pbeg = 0
    prod = 1
    for p in range(7, v + 1):
        if not isp[p]:
            continue
        if p <= Q:
            prod *= p
            pbeg += 1
            primes.append(p)
        pp = P(p)
        for t in range(8):
            j = p if p <= Q else p * p
            while j % 30 != rs[t]:
                j += p * 2
            pp.pos[t] = j // 30
        sprimes.append(pp)

    pre = [0xFF] * prod
    for pi in range(pbeg):
        pp = sprimes[pi]
        p = pp.p
        for t in range(8):
            m = ~(1 << t) & 0xFF
            for i in range(pp.pos[t], prod, p):
                pre[i] &= m

    block_size = ((L + prod - 1) // prod) * prod
    block = [0] * block_size
    M = (N + 29) // 30

    for beg in range(0, M, block_size):
        end = min(M, beg + block_size)
        for i in range(beg, end, prod):
            block[i:end] = pre[:end - i]
        if beg == 0:
            block[0] &= 0xFE
        for pi in range(pbeg, len(sprimes)):
            pp = sprimes[pi]
            p = pp.p
            for t in range(8):
                i = pp.pos[t]
                m = ~(1 << t) & 0xFF
                while i < end:
                    block[i] &= m
                    i += p
                pp.pos[t] = i
        for i in range(beg, end):
            m = block[i]
            while m > 0:
                bit = (m & -m)
                bit_index = (bit.bit_length() - 1)
                primes.append(i * 30 + rs[bit_index])
                m &= m - 1

    primes = [p for p in primes if p <= N]
    return primes

def is_pandigital(x: int) -> bool:
    s = str(x)
    n = len(s)
    target = ''.join(str(i) for i in range(1, n + 1))
    return ''.join(sorted(s)) == target

def main():
    N = 10**7
    primes = sieve(N)
    primes_set = set(primes)
    max_pandigital = -1
    for p in primes:
        if is_pandigital(p):
            if p > max_pandigital:
                max_pandigital = p
    print(max_pandigital)

if __name__ == "__main__":
    main()