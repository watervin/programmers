def solution(numbers, target):
    answer = 0
    queue = [0]
    
    for i in numbers:
        temp =[]
        for j in queue:
            temp.append(j + i)
            temp.append(j - i)
        queue = temp
    
    return queue.count(target)