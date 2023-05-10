from collections import defaultdict

def solution(id_list, report,k):
    user = defaultdict(set) # user별 신고한 id 저장
    declare = defaultdict(int) # user별 신고당한 횟수 저장
	
    for r in set(report):
        u_id, d_id = r.split(' ') # 문자열 나누기
        user[u_id].add(d_id)      # 신고자가 신고한 id 추가
        declare[d_id] += 1        # 신고당한 id의 신고 횟수 추가
    
    res = []
    for i in id_list: # user가 신고한 id가 k번 이상 신고 당했으면, 받을 메일 추가
        res.append(sum(1 for u in user[i] if declare[u]>=k))
        
    return res
        