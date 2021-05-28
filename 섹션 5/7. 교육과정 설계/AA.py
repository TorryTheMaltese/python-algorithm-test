import sys
import copy

# sys.stdin = open("in2.txt", "rt")

required_subject = list(input())
n = int(input())
class_plan = list()

for _ in range(n):
    class_plan.append(list(input()))


def check_class_plan(class_list):
    tmp = copy.deepcopy(required_subject)
    while len(tmp) > 0:
        # print(first, class_list[0])
        if len(class_list) > 0:
            first = class_list[0]
            if tmp[0] == first:
                tmp.pop(0)
                class_list.pop(0)
            else:
                class_list.pop(0)
        else:
            return False
    return True


for i in range(n):
    if check_class_plan(class_plan[i]):
        print('#', i + 1, ' YES')
    else:
        print('#', i + 1, ' NO')


# print(required_subject)
# print(class_plan)
