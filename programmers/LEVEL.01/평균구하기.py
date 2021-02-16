# 첫 번째 풀이, numpy.mean 함수를 통해 평균을 구함.
# 0.06ms ~ 0.42ms / 27.8MB
import numpy

def solution(arr):
    answer = 0
    answer= numpy.mean(arr)
    return answer

# 두 번째 풀이, 내장함수 sum과 len 함수를 사용해 평균을 구함
# 0.00ms ~ 0.01ms / 10.2MB
def solution(arr):
    answer = 0
    answer = sum(arr) / len(arr)
    return answer

# 세 번째 풀이, ststistics.mean 함수 사용해 평균 구함
# 0.06ms ~ 0.08ms  11.3MB
import statistics

def solution(arr):
    answer = 0
    answer = statistics.mean(arr)
    return answer

# 네 번째 풀이, 함수를 사용하지 않고 풀어서 평균을 구함
# 0.00ms ~ 0.01ms / 10.3MB
def solution(arr):
    answer = 0
    length = 0
    summary = 0
    for i in arr:
        summary += i
        length += 1
    answer = summary / length
    return answer