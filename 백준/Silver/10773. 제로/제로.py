import sys
input = sys.stdin.readline

st = []
for _ in range(int(input())):
    i = int(input())
    st.append(i) if i != 0 else st.pop()
        
print(sum(st))