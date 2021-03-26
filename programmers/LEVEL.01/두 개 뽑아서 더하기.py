import itertools

def solution(numbers):
    answer = []
    temp = []
    temp = itertools.combinations(range(len(numbers)), 2)
    print(temp)
    for i in temp:
        answer.append(numbers[i[0]] + numbers[i[1]])
        print(numbers[i[0]], numbers[i[1]])
    answer = sorted(list(set(answer)))
    return answer

print(solution([5,0,2,7]))