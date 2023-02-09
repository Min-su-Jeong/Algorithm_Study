n = int(input())
lst = []

for _ in range(n):
    age, name = map(str, input().split())
    lst.append((int(age), name))   
lst.sort(key = lambda x : x[0])

for i in lst:
    print(i[0], i[1])