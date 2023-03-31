def solution(id_pw, db):
    # id: key, pw: value로 변환하여 비교
    db_dict = {d[0]: d[1] for d in db} 
    
    # id가 존재하는 경우
    if id_pw[0] in db_dict:
        if id_pw[1] == db_dict[id_pw[0]]:
            return "login"
        else:
            return "wrong pw"
        
    # id가 존재하지 않는 경우
    else:
        return "fail"