S = input()

for A in range(1, 1000):
    current = ""
    B = A
    
    while len(current) < len(S):
        current += str(B)
        B += 1
    
    if current == S:
        print(A, B - 1)
        break