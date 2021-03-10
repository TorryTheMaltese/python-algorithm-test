# import sys
#
# sys.stdin = open("in1.txt", "rt")

# ------------ my solution ------------
# text = input()
# num_string = ""
#
# for t in text:
#     if 48 <= ord(t) <= 57:
#         num_string = num_string + t
#
# num = int(num_string)
# print(num)
#
# cnt = 0
# for i in range(1, num + 1):
#     if num % i == 0:
#         cnt += 1
# print(cnt)
# -------------------------------------

text = input()
num_string = ""

for t in text:
    if t.isdecimal():
        num_string += t

num = int(num_string)
print(num)

cnt = 0
for i in range(1, num + 1):
    if num % i == 0:
        cnt += 1
print(cnt)
