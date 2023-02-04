a, b = int(input()), 2

while True:
    if a == 1 or a == 2:
        print(a)
        break
    b *= 2
    if (a <= b):
        print((a - (b // 2)) *2)
        break