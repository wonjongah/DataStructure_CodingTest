import sys

# 숫자 커질 경우, sys.stdin.readline() 사용
n = int(sys.stdin.readline())
array = [0] * 10001

for i in range(n):
    data = int(sys.stdin.readline())
    # 인덱스에 해당하는 개수 증가
    array[data] += 1

for i in range(10001):
    # 숫자가 등장했다면
    if array[i] != 0:
        # 등장한 개수만큼 인덱스 출력
        for j in range(array[i]):
            print(i)