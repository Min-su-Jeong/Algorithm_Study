from collections import defaultdict

def solution(weights):
    res = 0
    person = defaultdict(int)
    for w in weights:
        # 한 사람의 몸무게 : w 가정 / w, 2w, 1/2w, 2/3w, 3/2w, 4/3w, 3/4w의 
        # 몸무게를 지닌 사람들과 시소 짝꿍 가능
        res += person[w] + person[w*2] + person[w/2] + person[(w*2)/3] + person[(w*3)/2] + person[(w*4)/3] + person[(w*3)/4]
        person[w] += 1
    return res