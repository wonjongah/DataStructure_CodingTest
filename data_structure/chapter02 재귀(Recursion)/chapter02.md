#### 2-1 함수의 재귀적 호출의 이해



- **재귀함수**의 기본적인 이해



재귀함수 -> 함수 내에서 자기 자신을 다시 호출하는 함수를 의미한다.



```c
void Recursive(void){
printf("Recursive call! \n");
Recursive(); // 자신을 호출
}
```



그렇다면 위 형태의 함수호출은 어떻게 이해해야 할까? 

호출 Recursive();를 만나면 다시 void Recursive(void){}로 재진입을 하는 걸까?

완료되지 않은 함수를 다시 호출하는 것이 가능하다. Recursive 함수가 호출되면, Recursive 함수의 복사본이 만들어져 본사본이 실행되는 구조로 재귀함수의 호출이 진행된다. 

즉 원본 함수가 하나 있고, 재귀함수 호출을 하게 되면 원본 함수의 복사본 함수를 실행시킨다는 뜻이다.

실제로 함수를 구성하는 명령문은 CPU로 이동되어(복사되어) 실행된다. 그런데 이 명령문은 얼마든지 CPU로 이동이(복사가) 가능하기 때문에 Recursive 함수가 완료하지 않은 상태에서 다시 Recursive 함수 앞 부분에 위치한 명령문을 CPU로 이동시키는 것은 문제가 되지 않기 때문에 재귀적인 함수 호출이 가능한 것이다.



```c
#include <stdio.h>

void Recursive(int num){

    if(num <= 0){   // 재귀 탈출 조건
        return;     // 재귀 탈출
    }
    printf("Recursive call! %d \n", num);
    Recursive(num-1);
}

int main(void){
    Recursive(3);
    return 0;
}
```



마지막 호출에서 return 0;을 만나고 돌아가면서 반환을 하는 형식이다. 

이렇듯 재귀함수를 정의할 때 탈출조건을 구성하는 것은 매우 중요한 일이다.



- 재귀함수의 디자인 사례



재귀함수는 자료구조나 알고리즘의 어려운 문제를 단순화하는데 중요한 수단이다. 무엇보다 재귀함수가 있기 때문에 재귀적인 수학적 수식을 그대로 옮길 수 있다. 



예시로 팩토리얼의 재귀적 특성을 보자.

```
n! = n * (n-1) * (n-2) * ....... * 2 * 1

=> n * (n-1)!
```



정수 n팩토리얼은 정수 n과 n-1 팩토리얼의 곱으로 표현할 수 있으므로, n팩토리얼 f(n)은 다음과 같다.



```
f(n) -> n * f(n-1)  - n >= 1
     -> 1 			   - n = 0 (0!은 1이므로)
```



#### 2-2 재귀의 활용



- 피보나치 수열(Fibonacci Sequence)



피보나치 수열은 재귀적인 형태를 띠는 대표적 수열로서 다음과 같이 전개된다.



```
0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ....
```



앞의 두 항을 더해서 현재의 수를 만들어가는 수열이다. 때문에 처음 두 개의 수 0과 1이 주어진 상태에서 수를 만들어가게 된다.

수열 n번째 값 = 수열 n-1번째 값 + 수열 n-2번째 값

따라서 피보나치 수열의 n번째 위치의 값을 반환하는 함수는 다음과 같이 표현한다.



```
fib(n) => 0 (n = 1)
	   => 1 (n = 2)
	   => fib(n-1) + fib(n-2)
```



```c
#include <stdio.h>

int Fibo(int n){
    
    if(n == 1){
        return 0;
    }else if(n == 2){
        return 1;
    }else{
        return Fibo(n-1) + Fibo(n-2);
    }
}

int main(void){

    int i;
    for(i = 1; i < 15; i++){
        printf("%d ", Fibo(i));
    }

    return 0;
}
```



위 예제는 피보나치 수열의 1번째 값부터 14번째 값까지 출력하고 있다. 

보통 소스코드를 분석할 때, 이 함수가 호출되고, 그 다음에 저 함수가 호출이 되면서, 마지막으로 이 함수가 호출된다라고 분석한다.

즉, 함수의 호출순서가 파악되지 않으면서 코드를 이해했다고 생각하지 않거나 찜찜해하는 경향이 있다.

위와 같은 재귀함수의 호출 순서도 100% 나열하려 노력하지 않아도 문제를 수식적으로 표현하고 코드로 옮겼다면 코드를 완벽히 이해한 셈이다.

재귀함수는 매우 많은 수의 함수호출을 동반한다.

```c
return Fibo(n-1) + Fibo(n-2);
```

를 보면 두 개의 Fibo 함수가 다시 호출되는데, + 연산자의 왼편에 있는 Fibo 함수호출이 완료되어야 비로소 + 연산자의 오른편에 있는 Fibo 함수호출이 진행된다. 

즉, Fibo(7) -> Fibo(6) + Fibo(5) => Fibo(6) 완료 후 => Fibo(5)



- 이진 탐색 알고리즘의 재귀적 구현



이진 탐색 알고리즘은 탐색 대상을 찾을 때까지 동일한 패턴을 반복하기 때문에 재귀적으로 충분히 구현 가능하다.

1. 탐색 범위의 중앙에 목표 값이 저장되었는지 확인
2. 저장되지 않았다면 탐색 범위를 반으로 줄여서 다시 탐색 시작

그리고 탐색의 실패의 조건은 first가 last보다 커지는 경우이다.

while -> 재귀함수로 변경



```c
#include <stdio.h>

int BSearchRecur(int ar[], int first, int last, int target){

    int mid;

    if(first > last){
        return -1;
    }
    mid = (first + last) / 2;

    if(ar[mid] == target){
        return mid;
    }else if(target < ar[mid]){ // 타겟이 중간값보다 작으면, last를 mid - 1로 지정하고 다시 탐색
        return BSearchRecur(ar, first, mid-1, target);
    }else{ // 타겟이 중간값보다 크면 first를 mid + 1로 지정하고 다시 탐색
        return BSearchRecur(ar, mid + 1, last, target);
    }
}

int main(void){

    int arr[] = {1,3,5,7,9};
    int idx;

    idx = BSearchRecur(arr, 0, sizeof(arr)/sizeof(int)-1, 7);
    if(idx == -1){
        printf("탐색 실패 \n");
    }else{
        printf("타겟 저장 인덱스: %d \n", idx);
    }

    idx = BSearchRecur(arr, 0, sizeof(arr)/sizeof(int)-1, 4);
    if(idx == -1){
        printf("탐색 실패 \n");
    }else{
        printf("타겟 저장 인덱스: %d \n", idx);
    }
    }
```



#### 2-3 하노이 타워 : The Tower of Hanoi



- 하노이 타워 문제의 이해



하노이 타워 문제는 하나의 막대에 쌓여 있는 원반을 다른 하나의 원반에 그대로 옮기는 방법에 관한 것이다.

![스크린샷(117)](https://user-images.githubusercontent.com/50413112/104160329-4bb33380-5434-11eb-820c-ad4625762778.png)

다음 제약 조건을 만족시켜야 한다.

원반은 한 번에 하나씩만 옮길 수 있다. 그리고 옮기는 과정에서 작은 원반의 위에 큰 원반이 올려져서는 안 된다.

원반의 개수가 늘어날 수록 일련의 과정이 반복된다. 즉, 재귀이므로 그 일련의 과정을 파악하면 된다.



- 하노이 타워의 반복패턴 연구



가장 아래의 제일 큰 원반을 C로 옮기는 것이 우선이다. 그러기 위해선 두 번째 막대에 위에서 마지막 - 1번째까지의 원반을 옮겨야 한다. 

1. 작은 원반 n-1개를(맨 아래의 원반을 제외한 나머지 원반을) A에서 B로 이동
2. 큰 원반(맨 아래 원반) 1개를 A에서 C로 이동
3. 작은 원반(B로 옮겨진 원반) n-1개를 B에서 C로 이동

이렇듯 원반 n개 이동 문제는 원반 n-1개를 이동하는 문제로, n-2개를 이동하는 문제로 세분화되며, 결국엔 원반 1개를 이동하는 쉬운 문제로 세분화된다.



```c
#include <stdio.h>

void HanoiTowerMove(int num, char from, char by, char to){
    // from에 꽂혀있는 num개의 원반을 by를 거쳐서 to로 이동

    if(num == 1)  // 이동할 원반의 수가 1개라면, 탈출 조건
    {
        printf("원반1을 %c에서 %c로 이동 \n", from, to);
    }else{
        HanoiTowerMove(num-1, from, to, by); // 3단계 중 1단계
        // n-1개의 원반을 A에서 B로
        printf("원반%d을 %c에서 %c로 이동 \n", num, from, to); // 3단계 중 2단계
        // 마지막 원반을 A에서 C로
        HanoiTowerMove(num-1, by, from, to);  // 3단계 중 3단계
        // n-1개의 원반을 B에서 C로
    }
}

int main(void){
    // 막대A의 원반 3개를 막대 B로 경유하여 막대 C로 옮기기
    HanoiTowerMove(3, 'A', 'B', 'C');
    return 0;
}
```

