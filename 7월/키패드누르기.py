import math
def solution(numbers, hand):
    
    answer = ''
     # 키패드 좌표료 변경
    dic = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*':[3, 0], 0: [3, 1], '#': [3, 2]}
    
    left_location = dic['*']
    right_location = dic['#']
    
    for i in numbers:
        location = dic[i]
        if i in [1,4,7]:
            answer += 'L'
            left_location = location
        elif i in [3,6,9]:
            answer += 'R'
            right_location = location
        else:
            l = 0
            r = 0
            for a,b,c, in zip(left_location,right_location,location):
                l += abs(a-c)
                r += abs(b-c)
            if l < r:
                answer += 'L'
                left_location = location
            elif l > r:
                answer += 'R'
                right_location = location
            else:
                if hand == "left":
                    answer += 'L'
                    left_location = location
                else:
                    answer += 'R'
                    right_location = location
                    
    return answer