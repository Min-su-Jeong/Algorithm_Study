import re

def solution(new_id):
    ret = new_id
    ret = ret.lower()
    ret = re.sub('[^a-z0-9\-_.]', '', ret)
    ret = re.sub('\.+', '.', ret)
    ret = re.sub('^[.]|[.]$', '', ret)
    ret = 'a' if len(ret) == 0 else ret[:15]
    ret = re.sub('^[.]|[.]$', '', ret)
    ret = ret if len(ret) > 2 else ret + "".join([ret[-1] for i in range(3-len(ret))])
    
    return ret