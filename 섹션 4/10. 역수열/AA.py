# import sys
#
# sys.stdin = open("in1.txt", "rt")

n = int(input())
reversed_nums = list(map(int, input().split()))
nums = [n + 1] * n

for index, num in enumerate(reversed_nums):
    cnt = 0
    for i in range(n):
        if cnt == num and nums[i] > n:
            nums[i] = index + 1
            break
        if nums[i] > (index + 1):
            cnt += 1

print(*nums)
