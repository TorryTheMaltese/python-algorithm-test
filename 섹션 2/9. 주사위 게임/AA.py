# import sys
#
# sys.stdin = open("in1.txt", "rt")

nums = int(input())
total = 0

for num in range(nums):
    first, second, third = map(int, input().split())
    tmp = 0
    if first == second == third:
        tmp = 10000 + (first * 1000)
    elif first == second | first == third:
        tmp = 1000 + (first * 100)
    elif second == third:
        tmp = 1000 + (second * 100)
    else:
        tmp = first * 100
        if tmp < second * 100:
            tmp = second * 100
        if tmp < third * 100:
            tmp = third * 100

    if total < tmp:
        total = tmp

print(total)
