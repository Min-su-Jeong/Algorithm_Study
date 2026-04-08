def intToTime(i: int):
    h = i // 60
    m = i % 60
    return f"{h:02d}:{m:02d}"

def timeToInt(s: str):
    h, m = map(int, s.split(':'))
    return h * 60 + m

def addTime(time):
    return timeToInt(time) - timeToInt(prev)

if __name__ == "__main__":
    N = int(input())

    ret1, ret2 = 0, 0
    t1, t2 = 0, 0
    prev = ""

    for _ in range(N):
        tno, time = input().split()

        if t1 > t2:
            ret1 += addTime(time)
        elif t1 < t2:
            ret2 += addTime(time)

        if tno == "1": t1 += 1
        else: t2 += 1
        prev = time

    if t1 > t2: ret1 += addTime("48:00")
    elif t1 < t2: ret2 += addTime("48:00")

    print(intToTime(ret1))
    print(intToTime(ret2))