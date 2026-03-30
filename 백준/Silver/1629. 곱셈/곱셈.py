def modular(A, B, C):
    if B == 1:
        return A % C
    
    ret = modular(A, B // 2, C)
    ret = (ret * ret) % C

    if (B % 2 == 1):
        ret = (ret * A) % C
    
    return ret

if __name__ == "__main__":
    A, B, C = map(int, input().split())

    print(modular(A, B, C))