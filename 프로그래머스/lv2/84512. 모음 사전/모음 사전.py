word_list = []
words = 'AEIOU'
    
# dfs를 통해 규칙에 따른 모음 사전 만들기
def dfs(cnt, w):
    if cnt == 5:
        return
    for i in range(len(words)):
        word_list.append(w + words[i])
        dfs(cnt+1, w + words[i])
            
def solution(word):
    dfs(0,"")
    return word_list.index(word) + 1