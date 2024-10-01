def solution(phoneBook):
    hashMap = {}
    for pb in phoneBook:
        hashMap[pb] = True
        
    for pb in phoneBook:
        arr = ''
        for s in pb:
            arr += s

            if arr in hashMap and arr != pb:
                return False
            
    return True