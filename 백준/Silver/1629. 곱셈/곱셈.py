def modular(a, b, c):
    if b == 1:
        return a % c

    ret = modular(a, b // 2, c)
    ret = (ret * ret) % c

    if b % 2 == 1:
        ret = (ret * a) % c

    return ret

a, b, c = map(int, input().split())
print(modular(a, b, c))