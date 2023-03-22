def solution(dot):
    x, y = dot[0], dot[1]
    # if ~ elif ~ else 한 줄 요약
    return 1 if (x>0 and y>0) else 2 if (x<0 and y>0) else 4 if (x>0 and y<0) else 3