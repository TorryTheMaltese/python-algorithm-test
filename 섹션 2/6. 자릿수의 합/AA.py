# import sys
#
# sys.stdin = open("in1.txt", "rt")

n = int(input())
nums = list(map(int, input().split()))
max_sum = 0
res = 0


def digit_sum(x):
    word = str(x)
    sum_tmp = 0
    for w in word:
        sum_tmp += int(w)
    return sum_tmp


for i in range(n):
    tmp = digit_sum(nums[i])
    if tmp > max_sum:
        max_sum = tmp
        res = nums[i]

print(res)
