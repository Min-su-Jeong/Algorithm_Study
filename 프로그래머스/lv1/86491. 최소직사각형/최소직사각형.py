def solution(sizes):
    wlist, hlist = [], []
    for w, h in sizes:
        if h > w:
            wlist.append(h)
            hlist.append(w)
        else:
            wlist.append(w)
            hlist.append(h)
    
    return max(wlist) * max(hlist)
            