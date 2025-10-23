
def hai(x):
    nums = [x * i for i in range(1, 7)]
    sorted_nums = [''.join(sorted(str(num))) for num in nums]
    return all(s == sorted_nums[0] for s in sorted_nums)


N=10**7
for _ in range(1,N):
    if hai(_):
        print(_)
        break