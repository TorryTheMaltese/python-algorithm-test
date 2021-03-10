# import sys
#
# sys.stdin = open("in4.txt", "rt")

n = int(input())
grades = list(map(int, input().split()))
avg = round(sum(grades) / n)

gap = grades[0]-avg
cnt = 0

for i in range(n):
    tmp = grades[i]-avg
    # print(f"평균 : {avg}, {i+1}번째 값 : {grades[i]}, 차이의 절댓값 : {abs(tmp)}")
    if abs(tmp) < abs(gap):
        gap = tmp
        cnt = i
    elif (abs(gap) == abs(tmp)) & (tmp > gap):
        gap = tmp
        cnt = i


print(f'{round(avg)} {cnt+1}')
