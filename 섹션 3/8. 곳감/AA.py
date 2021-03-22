# import sys
#
# sys.stdin = open("in1.txt", "rt")

n = int(input())
arr = [list(map(int, input().split())) for i in range(n)]
m = int(input())

for i in range(m):
    row_num, is_right, rotation_num = map(int, input().split())
    row_num -= 1
    rotation_num = rotation_num % n
    if is_right:
        for _ in range(rotation_num):
            arr[row_num].insert(0, arr[row_num].pop())
    else:
        for _ in range(rotation_num):
            arr[row_num].append(arr[row_num].pop(0))

res = 0
left = 0
right = n

for i in range(n):
    for j in range(left, right):
        res += arr[i][j]
    if i >= n // 2:
        left -= 1
        right += 1
    else:
        left += 1
        right -= 1

# print('\n'.join(' '.join(map(str, sl)) for sl in arr))
print(res)
