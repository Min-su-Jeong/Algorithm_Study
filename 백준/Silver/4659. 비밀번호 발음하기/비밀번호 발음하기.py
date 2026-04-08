import sys
input = lambda: sys.stdin.readline().rstrip()

def check(string):
    prev = string[0]
    includeV, flag = False, True
    ccnt, vcnt = 0, 0

    for idx, s in enumerate(string):
        if s in "aeiou":
            includeV = True
            vcnt += 1
            ccnt = 0
        else:
            ccnt += 1
            vcnt = 0

        if ccnt == 3 or vcnt == 3:
            flag = False

        if idx >= 1 and prev == s and (s != "e" and s != "o"):
            flag = False
        
        prev = s

    if not includeV: return False
    if not flag: return False
    return True

while True:
    s = input()
    if s == "end":
        break
    
    ret = check(s)
    if ret:
        print(f"<{s}> is acceptable.")
    else:
        print(f"<{s}> is not acceptable.")