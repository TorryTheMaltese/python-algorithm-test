# import sys
#
# sys.stdin = open("in2.txt", "rt")

n = int(input())
nums = list(map(int, input().split()))
reversed_num = list()


def reverse(x):
    word = str(x)
    tmp = list()
    for i in word:
        tmp.append(i)
    tmp.reverse()
    new_word = ''.join(tmp)
    return int(new_word)


def isPrime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    else:
        return True


for num in nums:
    if isPrime(reverse(num)):
        reversed_num.append(reverse(num))

print(*reversed_num, sep=" ")
