import sys

# sys.stdin = open("in2.txt", "rt")

prefix = list(map(str, input()))
stack = list()
result = ""
# print(*prefix)

for pre in prefix:
    if pre.isdecimal():
        result = result + pre
    elif pre=='(':
        stack.append(pre)
    elif pre == '+' or pre == '-':
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.append(pre)
    elif pre == '*' or pre == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            result += stack.pop()
        stack.append(pre)
    elif pre == ')':
        while stack and stack[-1] != '(':
            result += stack.pop()
        stack.pop()

while stack:
    result += stack.pop()

print(result)
