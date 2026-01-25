alpha = [0] * 26

S = input()

for s in S:
    alpha[ord(s) - ord('a')] += 1

for a in alpha:
    print(a, end=' ')