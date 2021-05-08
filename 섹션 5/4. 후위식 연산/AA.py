import sys
# sys.stdin = open("in1.txt", "rt")

postfix = input()
stack = []

for e in postfix:
    if e.isdecimal():
        stack.append(e)
    else:
        if e=='+':
            right = int(stack.pop())
            left = int(stack.pop())
            res = left + right
            stack.append(res)
        elif e=='-':
            right = int(stack.pop())
            left = int(stack.pop())
            res = left - right
            stack.append(res)
        elif e=='*':
            right = int(stack.pop())
            left = int(stack.pop())
            res = left * right
            stack.append(res)
        elif e=='/':
            right = int(stack.pop())
            left = int(stack.pop())
            res = left / right
            stack.append(res)

# print(postfix)
print(stack.pop())