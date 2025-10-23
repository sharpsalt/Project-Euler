def collatz_length(n, memo):
    if n == 1:
        return 1
    if n in memo:
        return memo[n]
    if n & 1:
        memo[n] = 1 + collatz_length(3 * n + 1, memo)
    else:
        memo[n] = 1 + collatz_length(n // 2, memo)
    return memo[n]

memo={}
max_len=0
num=0

for i in range(1,1_000_000):
    length=collatz_length(i,memo)
    if length>max_len:
        max_len=length
        num=i

print(num,max_len)
