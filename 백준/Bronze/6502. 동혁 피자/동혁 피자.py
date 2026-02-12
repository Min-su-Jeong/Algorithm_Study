idx = 1
while True:
    s = input().split()
    if s[0] == "0":
        break

    r, w, l = map(int, s)
    if w * w + l * l <= (2 * r) * (2 * r):
        print(f"Pizza {idx} fits on the table.")
    else:
        print(f"Pizza {idx} does not fit on the table.")
    
    idx += 1