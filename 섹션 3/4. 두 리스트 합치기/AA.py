# import sys
#
# sys.stdin = open("in1.txt", "rt")

a_list_size = int(input())
a_list = list(map(int, input().split()))

b_list_size = int(input())
b_list = list(map(int, input().split()))

result_list = a_list + b_list
result_list.sort()

print(*result_list, sep=" ")
