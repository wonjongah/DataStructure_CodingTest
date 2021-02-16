# for문을 돌려서 이전과 같지 않다면 answer 배열에 추가하는 형식으로
# 연속적으로 나타나는 숫자를 제거한 배열을 만들었다.
# 0.01ms ~ 44.58ms / 10.2MB ~ 27.9MB
# 정확성: 71.9, 효율성: 28.1

def solution(arr):
    answer = []
    before = -1
    for i in arr:
        if i != before:
            answer.append(i)
        before = i
    return answer