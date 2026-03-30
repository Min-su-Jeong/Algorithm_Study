N = int(input())

def check(words):
    stk = []

    for w in words:
        if stk and stk[-1] == w:
            stk.pop()
        else:
            stk.append(w)

    if stk:
        return False
    else:
        return True

ret = 0   
for _ in range(N):
    words = input()

    if check(words):
        ret += 1

print(ret)