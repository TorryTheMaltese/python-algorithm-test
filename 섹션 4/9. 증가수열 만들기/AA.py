# import sys
#
# sys.stdin = open("in5.txt", "rt")

n = int(input())
nums = list(map(int, input().split()))
res = []
last = 0

while len(nums) > 0:
    if len(nums) > 1:
        left = nums[0]
        right = nums[-1]
        if left < right:
            if left < last:
                if right > last:
                    nums.pop()
                    res.append("R")
                    last = right
                else:
                    break
            else:
                nums.pop(0)
                res.append("L")
                last = left
        else:
            if right < last:
                if left > last:
                    nums.pop(0)
                    res.append("L")
                    last = left
                else:
                    break
            else:
                last = nums.pop()
                res.append("R")
    else:
        if nums[0] > last:
            nums.pop()
            res.append("L")
        else:
            nums.pop()
            break

print(len(res))
print(''.join(map(str, res)))
