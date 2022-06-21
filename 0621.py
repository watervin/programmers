def solution(lottos, win_nums):
    
    rank = [6,6,5,4,3,2,1]
    cnt = lottos.count(0)
    result = 0
    for i in lottos:
        if i in win_nums:
            result += 1
    
    return rank[cnt+result],rank[result]