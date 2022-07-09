def solution(answers):
    answer = []
    number = [0] * 3 
    n1 = [1, 2, 3, 4, 5] 
    n2 = [2, 1, 2, 3, 2, 4, 2, 5] 
    n3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if answers[i] == n1[i%5]:
            number[0] += 1
        if answers[i] == n2[i%8]:
            number[1] += 1
        if answers[i] == n3[i%10]:
            number[2] += 1

    winner = max(number) 
    for i in range(len(number)):
        if number[i] == winner:
            answer.append(i+1)
    return answer