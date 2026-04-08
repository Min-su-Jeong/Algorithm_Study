M = int(input())

ret = []
for _ in range(M):
    string = input()

    digit = ""
    for s in string:
        if s.isdigit():
            digit += s
        else:
            if digit:
                ret.append(int(digit))
                digit = ""

    if digit:
        ret.append(int(digit))

ret.sort()
print(*ret, sep='\n')