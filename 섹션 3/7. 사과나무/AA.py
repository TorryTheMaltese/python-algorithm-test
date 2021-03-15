# import sys
#
# sys.stdin = open("in1.txt", "rt")

n = int(input())
a = list()
total = 0

for i in range(0, n):
    a.append(list(map(int, input().split())))

# for i in range(0, n):
#     print(a[i])

i = 1
num = int(n / 2)
# print(num)

for i in range(0, n):
    if i > num:
        gap = i - num
        total += sum(a[i][gap:-gap])
    else:
        total += sum(a[i][num - i:num + i+1])

print(total)
