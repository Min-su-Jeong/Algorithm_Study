import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

ret = []
alpha = [0] * 26

for _ in range(N):
    s = input()
    alpha[ord(s[0]) - ord('a')] += 1

for i in range(len(alpha)):
    if alpha[i] < 5:
        continue

    ret.append(chr(i+ord('a')))

if ret:
    print(''.join(ret))
else:
    print("PREDAJA")