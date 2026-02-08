N = int(input())
ret = []

for _ in range(N):
    s = input()
    
    digit = ""
    for i in range(len(s)):
        if s[i].isdigit():
            digit += s[i]
        else:
            if digit:
                ret.append(int(digit))
                digit = ""

    if digit:
        ret.append(int(digit))

ret.sort()
for i in ret:
    print(i)