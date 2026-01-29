N = int(input())
university = {}

for i in range(N):
    s = input()
    university[s] = i

if university["yonsei"] < university["korea"]:
    print("Yonsei Won!")
else:
    print("Yonsei Lost...")