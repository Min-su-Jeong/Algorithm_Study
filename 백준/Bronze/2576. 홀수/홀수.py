odd = []
for i in range(7):
    num = int(input())
    if num%2:
        odd.append(num)
        
if not len(odd):
    print(-1)
else:
    print(sum(odd))
    print(min(odd))