# import sys
#
# sys.stdin = open("in2.txt", "rt")

sticks = list(map(str, input()))
stack = []
cnt = 0


for i in range(len(sticks)):
    pivot = sticks[i]

    if pivot == '(':
        stack.append(pivot)
    elif pivot == ')':
        stack.pop()
        if sticks[i-1] == '(':
            cnt += len(stack)
        else:
            cnt += 1

print(cnt)
