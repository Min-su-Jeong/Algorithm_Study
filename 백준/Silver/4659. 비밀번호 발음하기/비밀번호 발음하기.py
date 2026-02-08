while True:
    s = input()
    if s == "end":
        break
    
    prev = -1
    vcnt, ccnt = 0, 0
    avail, includeV = True, False

    for i in range(len(s)):
        idx = s[i]
        if s[i] in "aeiou":
            vcnt += 1
            ccnt = 0
            includeV = True
        else:
            vcnt = 0
            ccnt += 1

        if vcnt == 3 or ccnt == 3:
            avail = False

        if i >= 1 and prev == idx and (idx != 'e' and idx != 'o'): avail = False
        prev = idx

    if not includeV: avail = False
    if not avail:
        print(f"<{s}> is not acceptable.")
    else:
        print(f"<{s}> is acceptable.")