N = int(input())
suf, pre = input().split('*')

for _ in range(N):
    s = input()

    if len(s) < len(suf) + len(pre):
        print("NE")
        continue
    
    if s[:len(suf)] == suf and s[-len(pre):] == pre:
        print("DA")
    else:
        print("NE")