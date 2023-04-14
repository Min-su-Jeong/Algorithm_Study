def solution(array, commands):
    # commands의 각 리스트에서 i,j,k 값을 가져와 규칙에 따라 인덱싱하여 리스트로 반환
    return [sorted(array[c[0]-1:c[1]])[c[2]-1] for c in commands]
        
        