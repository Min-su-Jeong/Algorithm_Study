def timeToInt(s: str):
    h, m = map(int, s.split(':'))
    return h * 60 + m

def intToTime(i: int):
    h = i // 60
    m = i % 60
    return f"{h:02d}:{m:02d}"

def calcTime(time):
    return timeToInt(time) - timeToInt(prev)

if __name__ == "__main__":
    N = int(input())

    t1, t2 = 0, 0
    sum1, sum2 = 0, 0
    prev = ""

    for _ in range(N):
        tno, time = input().split()
        tno = int(tno)

        if t1 > t2:
            sum1 += calcTime(time)
        elif t1 < t2:
            sum2 += calcTime(time)

        if tno == 1: t1 += 1
        else: t2 += 1

        prev = time

    if t1 > t2: sum1 += calcTime("48:00")
    elif t1 < t2: sum2 += calcTime("48:00")

    print(intToTime(sum1))
    print(intToTime(sum2))