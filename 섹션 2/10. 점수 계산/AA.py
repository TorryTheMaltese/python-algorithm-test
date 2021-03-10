# import sys
#
# sys.stdin = open("in1.txt", "rt")

num = int(input())
grades = list(map(int, input().split()))

get_point = 0
add_point = 0

for grade in grades:
    if grade == 1:
        add_point += 1
    if grade == 0:
        add_point = 0
    get_point += add_point

print(get_point)
