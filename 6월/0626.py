def solution(absolutes, signs):

    answer = 0

    for i in range(len(absolutes)):
        if signs[i] == True :
            answer += absolutes[i]
        elif signs[i] == False :
            answer -= absolutes[i]
        else :
            print("잘못된 값")


    return answer