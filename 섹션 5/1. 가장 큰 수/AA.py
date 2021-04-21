# import sys
#
# sys.stdin = open("in5.txt", "rt")

num_string, m = map(int, input().split())
num_list = list(map(int, str(num_string)))
stack = []
i = 0

while (len(num_list) - 5) < len(num_list):
    if len(stack) < m:
        if i<len(num_list)-1:
            if num_list[i] < num_list[i + 1]:
                stack.append(num_list.pop(i))
                i = 0
            else:
                i += 1
        else:
            num_list = num_list[0:len(num_list)-m]
            break

    else:
        break

# print(num_list)
# print(stack)
print(''.join(map(str, num_list)))


