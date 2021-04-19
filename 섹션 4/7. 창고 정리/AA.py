# import sys
#
# sys.stdin = open("in1.txt", "rt")

l = int(input())
boxs = list(map(int, input().split()))
m = int(input())

for _ in range(m):
    boxs.sort(reverse=True)
    boxs[0] -= 1
    boxs[-1] += 1

boxs.sort(reverse=True)
print(boxs[0]-boxs[-1])
