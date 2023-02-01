n = int(input())
lst = []

for i in range(n):
    lst.append(input())
    
lst = list(set(lst))
lst.sort()
lst.sort(key=len)

for word in lst:
    print(word)