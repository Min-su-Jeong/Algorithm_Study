import sys
input = sys.stdin.readline

# Input
N = int(input())
words = [input().rstrip() for _ in range(N)]

# Variables
res = 0
num = 9
word_dict = {}

# Solution
for word in words:
    i = len(word) - 1

    for w in word:
        if w in word_dict:
            word_dict[w] += 10**i
        else:
            word_dict[w] = 10**i
        i -= 1

word_dict = sorted(word_dict.values(), reverse=True)
for i in word_dict:
    res += i * num
    num -= 1

# Output
print(res)