# import sys
# sys.stdin = open("in1.txt", "rt")

n = int(input())

for n in range(n):
    word = list(input().lower())
    is_palindrome = "YES"

    for i in range(round(len(word) / 2)):
        if word[i] != word[-(i + 1)]:
            is_palindrome = "NO"

    print(f'#{n + 1} {is_palindrome}')
