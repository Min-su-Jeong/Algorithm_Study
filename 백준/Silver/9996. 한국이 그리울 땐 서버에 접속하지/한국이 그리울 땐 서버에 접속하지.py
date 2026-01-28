N = int(input())
pre, suf = input().split("*")

def check(s: str) -> bool:
    if len(pre) + len(suf) > len(s):
        return False
    else:
        if s[:len(pre)] == pre and s[-len(suf):] == suf:
            return True
        else:
            return False

for _ in range(N):
    s = input()

    ret = check(s)
    if ret:
        print("DA")
    else:
        print("NE")