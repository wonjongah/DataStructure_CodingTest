### 3.1 당장 좋은 것만 선택하는 그리디



그리디(Greedy) 알고리즘은 단순하지만 강력한 알고리즘이다. 이름에서도 알 수 있듯이 어떠한 문제가 있을 때 단순 무식하게, 탐욕적으로 문제를 푸는 알고리즘이다. 여기서 탐욕적이라는 말은 '현재 상황에서 지금 당장 좋은 것만 고르는 방법'을 의미한다. 즉, 지금 좋은 걸 선택하며, 나중에 미칠 영향은 고려하지 않는다.

코딩 테스트에서의 그리디 알고리즘 문제 유형은 다른 알고리즘과 비교했을 때 '사전에 외우지 않아도 풀 수 있을 가능성이 높은 문제 유형'이라는 특징이 있다. 

보통 코딩 테스트에 출제되는 그리디 알고리즘 유형의 문제는 창의력, 문제를 풀기 위한 최소한의 아이디어를 떠올릴 수 있는 능력을 요구한다. <u>특정 문제를 만났을 때 단순히 현재 상황에서 가장 좋아보이는 것을 선택해도 문제를 풀 수 있는지 파악이 중요하다.</u>

그리디 알고리즘은 문제에서 '가장 큰 순서대로', '가장 작은 순서대로'와 같은 기준을 제시해준다. 대체로 정렬 알고리즘을 사용해야 만족시킬 수 있으므로 그리디 알고리즘 문제는 자주 정렬 알고리즘과 짝을 이뤄 출제된다.



#### 거스름돈

당신은 음식점의 계산을 도와주는 점원이다. 카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원짜리 동전이 무한히 존재한다고 가정한다. 손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러줘야 할 동전의 최소 개수를 구하라. 단, 거슬러 줘야 할 돈 N은 항상 10의 배수이다.



-> '가장 큰 화폐 단위부터 거슬러준다', 거슬러줘야 할 동전의 최소 개수이기 때문에.

먼저 500원으로 거슬러줄 수 있는 만큼 거슬러 준 후, 100, 50, 10원짜리 동전을 차례대로 거슬러 줄 수 있는 만큼 거슬러준다.



```python
def bigchange(n):
    count = 0
    coin_types = [500, 100, 50, 10]
    for coin in coin_types:
        count += n // coin # 해당 화폐로 거슬러줄 수 있는 동전의 개수 세기
        n %= coin
    return count

n = 1260
print(bigchange(n))
```



위의 코드의 시간 복잡도는 O(K), 즉 화폐의 종류만큼이다. 



- 그리디 알고리즘의 정당성



그리디 알고리즘으로 거스름돈 문제를 그리디 알고리즘으로 해결할 수 있는 이유는 가지고 있는 동전 중에서 큰 단위가 항상 작은 단위의 배수이므로 작은 단위의 동전을 종합해 다른 해가 나올 수 없기 때문이다.

대부분의 그리디 알고리즘 문제에서는 이처럼 문제 풀이를 위한 최소한의 아이디어를 떠올리고 이것이 정당한지 검토할 수 있어야 답을 도출할 수 있다. 

문제를 만났을 때, 바로 문제 유형을 파악하기 힘들다면 그리디 알고리즘을 의심하고, 해결법이 존재하는지 고민해야 한다. 

만약, 오랜 시간 고민해도 그리디 알고리즘으로 해결 방법을 찾을 수 없다면, 다이나믹 프로그래밍이나 그래프 알고리즘 등으로 문제를 해결할 수 있는지 고민해보는 것도 좋은 방법이다.

거스름돈의 화폐 단위가 서로 배수 형태가 아니라 무작위로 주어진 경우엔 다이나믹 프로그래밍으로 해결 가능하다.



#### 큰 수의 법칙



'큰 수의 법칙'은 일반적으로 통꼐 분야에서 다루어지는 내용이지만