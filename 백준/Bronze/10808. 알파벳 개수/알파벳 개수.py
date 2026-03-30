string = input()
alpha = [0] * 26

for s in string:
    alpha[ord(s) - 97] += 1

for a in alpha:
    print(a, end=' ')