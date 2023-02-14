l, res = int(input()), 0

for i, s in enumerate (input()):
    res += (ord(s) - 96) * (31**i) # 해시 함수
    
print(res)