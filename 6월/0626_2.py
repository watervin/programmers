def solution(participant, completion):
    answer = ''

    for i in range(len(participant)):
        if participant.count(participant[i]) == completion.count(participant[i]):
            pass
          
        else:
            answer = participant[i]

    return answer
