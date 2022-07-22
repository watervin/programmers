def solution(n):
    
    answer = ''
    while n:
        #나머자기 1이상일 때
        if n % 3:
            answer += str(n % 3)
            n //= 3
        else:
            answer += "4"
            n = n// 3 -1
            
    return answer[::-1]