words = input()

alpha = [0] * 26
for w in words:
    alpha[ord(w) - ord('A')] += 1

flag = 0
ret = ''
mid = ''
for i in range(26):
    if alpha[i] % 2 == 1:
        mid = chr(i + ord('A'))
        flag += 1

    if flag > 1:
        print("I'm Sorry Hansoo")
        exit()

for i in range(26):
    ret += chr(i + ord('A')) * (alpha[i] // 2)

ret = ret + mid + ret[::-1]

print(ret)