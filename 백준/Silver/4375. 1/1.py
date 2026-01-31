while True:
    try:
        n = int(input())
    except:
        break

    cnt, ret = 1, 1
    while True:
        if cnt % n == 0:
            print(ret)
            break
        else:
            cnt = cnt * 10 + 1
            cnt %= n
            ret += 1