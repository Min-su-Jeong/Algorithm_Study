T = int(input())

while T:
    N = int(input())

    ret = 0
    i = 5
    while i <= N:
        ret += N // i
        i *= 5

    print(ret)
    T -= 1