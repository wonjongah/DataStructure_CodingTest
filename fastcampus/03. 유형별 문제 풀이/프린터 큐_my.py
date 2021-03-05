num = int(input())

for i in range(num):
    # n = 문서의 개수
    # m = 궁금한 문서가 현재 큐에 몇 번째 놓여져 있는지
    n, m = list(map(int, input().split()))
    # 중요도
    imp = list(map(int, input().split()))
    # 중요도와 인덱스 한 튜플로 만듦
    imp = [(i, index) for index, i in enumerate(imp)]
    count = 0
    while True:
        # 맨 처음의 값이 imp의 가장 큰 값 중 앞쪽의 값과 같다면 cout ++
        if imp[0][0] == max(imp, key=lambda x: x[0])[0]:
            count += 1
            # 만일 첫 번째의 요소가 타겟 요소라면 출력하고 break
            if imp[0][1] == m:
                print(count)
                break
            # 아니라면 첫 번째 요소 pop
            else:
                imp.pop(0)
        # 출력 순서가 아니라면, 맨 앞의 요소를 pop한 값을 다시 append
        else:
            imp.append(imp.pop(0))