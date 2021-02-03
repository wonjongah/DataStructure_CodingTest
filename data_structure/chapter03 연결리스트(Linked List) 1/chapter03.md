#### 3-1 추상 자료형 : Abstract Data Type



- 컴퓨터 공학에서의 추상 자료형(Abstract Data Type)



간단히 ADT라고도 불리는 추상 자료형은 컴퓨터 공학에서 흔히 등장하는 용어이다.

여러 분야에서 형태의 차이를 보이지만, 큰 맥락에서 보면 한 개념이다.



- 자료구조에서의 추상 자료형



한 대화에서 지갑에 대한 추상 자료형을 추출해보면 다음과 같다.

-> 카드의 삽입

-> 카드의 추출

-> 동전의 삽입

-> 동전의 추출

-> 지폐의 삽입

-> 지폐의 추출



예를 들어 동전의 삽입은 다음 과정을 거쳐야 한다.

지갑을 열고 동전 주머니를 찾아서 동전 주머니의 지퍼를 내린다. 그리고 동전 주머니에 동전을 넣는다. 동전 주머니의 지퍼를 올린 다음 마지막으로 지갑을 닫는다.

즉, 위에 정리해놓는 것이 지갑이 제공하는 기능들이다.

이렇게 구체적인 기능의 완성 과정을 언급하지 않고, 순수하게 기능이 무엇인지 나열한 것을 가리켜 추상 자료형, 간단히 ADT라고 한다. 



```C
typedef struct _wallet{  // 동전 및 지폐 일부만을 대상으로 표현한 지갑
int coin100Num;  // 100원짜리 동전의 수
int bill5000Num;  // 5000원짜리 지폐의 수
}Wallet;
```

이렇게 C언어 기반 구조체를 정의했다면, 구조체를 기반으로 지갑을 의미하는 Wallet이라는 자료형을 정의했다고 이야기할 수 있다.

그러나 위의 구조체 정의만으로 Wallet이라는 자료형의 정의가 완성되는 것은 아니다. Wallet을 기반으로 하는 연산의 종류를 결정하는 것도 자료형 정의의 일부로 보아야 하고, 이런 연산의 종류가 결정되었을 때 자료형의 정의는 완성된다.

위에 언급된 연산은 Wallet을 기반으로 제공할 수 있는 기능 관련 연산을 의미한다.

-> 돈을 꺼내는 연산 -> int TakeOutMoney(Wallet * pw, int coinNum, int billNum);

-> 돈을 넣는 연산 -> void PutMoney(Wallet * pw, int coinNum, int billNum);

이렇듯 C언어에서는 구조체에서 필요로 하는 연산을 함수를 이용해 정의한다. 그리고 위의 연산 둘이 Wallet과 관련있는 연산의 전부라면 이 둘이 더해져서 Wallet에 대한 자료형의 정의는 완성이다.



결론은 자료형의 정의에 기능 혹은 연산과 관련된 내용을 명시할 수 있다는 것이다.

따라서 추상 자료형이라고 기능과 연산 내용을 명시할 수 없다는 생각은 잘못된 생각이다.



- 구조체 Wallet의 추상 자료형 정의



구초제 Wallet도 자료구조의 일종이다. 이는 지갑이라는 데이터를 표현한 결과이기 때문이다.

구체적인 기능의 완성과정을 언급하지 않고, 순수하게 기능이 무엇인지를 나열한 것을 가리켜 '추상자료형' 또는 ADT라고 한다.

```
// Wallet의 ADT

int TakeOutMoney(Wallet * pw, int coinNum, int billNum)
- 첫 번째 인자로 전달된 주소의 지갑에서 돈을 꺼낸다.
- 두 번째 인자로 꺼낼 동전의 수, 세 번째 인자로 꺼낼 지폐의 수를 전달한다.
- 꺼내고자 하는 돈의 총액이 반환된다. 그리고 그만큼 돈은 차감된다.

void putMoney(Wallet * pw, int coinNum, int billNum)
- 첫 번째 인자로 전달된 주소의 지갑에 돈을 넣는다.
- 두 번째 인자로 넣을 동전의 수, 세 번째 인자로 넣을 지폐의 수를 전달한다.
- 넣은 만큼의 동전과 지폐의 수가 증가한다.
```

추상자료형을 명시하는 데엔 명시해야 할 정보인 기능을 충분히 묘사하고 있다면 위와 같은 방법도 상관없다.

```c
int main(void){
Wallet myWallet; // 새 지갑
...
putMoney(&myWallet, 5, 10); // 돈을 넣는다.
...
ret = TakeOutMoney(&myWallet, 2, 5); // 돈을 꺼낸다.
...
}
```

Wallet을 기반으로 돈을 넣고 꺼내는데 있어 구조체 Wallet의 멤버가 어떻게 구성이 되어 있는지는 알 필요가 없다. 따라서 위의 경우 구조체 Wallet의 정의를 ADT에 포함시키는 것은 바람직하지 못한다.

굳이 필요 없다면 구조체의 멤버에 알 필요는 없고, 필요한 기능의 연산을 ADT에 추가하는 것이 바람직하다.



- 자료구조의 학습에 ADT의 정의를 포함한다.



리스트 자료구조의 학습 순서

1. 리스트 자료구조의 ADT를 정의한다.
2. ADT를 근거로 리스트 자료구조를 활용하는 main 함수를 정의한다.
3. ADT를 근거로 리스트를 구현한다.

리스트 사용자에게 사용방법 이외의 불필요한 방법까지 알도록 하지 않도록 내부 구현을 알지 못해도 활용할 수 있도록 구현하기 위해 ADT 정의가 필수다.



#### 3-2 배열을 이용한 리스트의 구현



- 리스트의 이해



리스트는 연결리스트를 의미하지 않는다.

리스트라는 자료구조는 구현 방법에 따라 다음과 같이 크게 두 가지로 나뉜다.

1. 순차 리스트 -> 배열을 기반으로 구현된 리스트
2. 연결 리스트 -> 메모리의 동적 할당을 기반으로 구현된 리스트

둘은 각각의 특성적 차이 때문에 ADT에 차이를 둘 것이고, ADT는 정의하는 사람, 즉 필요에 따라 ADT도 차이가 난다.

<u>리스트 자료구조는 데이터를 나란히 저장한다. 그리고 중복된 데이터의 저장을 막지 않는다.</u>

리스트는 중복을 허용하고, 이 특성은 리스트 ADT를 정의하는데 있어서 고려해야 할 요소이다.



- 리스트의 ADT



데이터를 어떻게 나란히 저장할지 정하는 것부터 시작하지 말고, 나란히 저장된다는 특성을 기반으로 제공해야 할 기능을 먼저 정의해야 한다.

```
// 리스트 자료구조의 ADT
void ListInit(List *plist);
- 초기화할 리스트의 주소 값을 인자로 전달한다.
- 리스트 생성 후 제일 먼저 호출되어야 하는 함수이다.

void LInsert(List *plist, LData data);
- 리스트에 데이터를 저장한다. 매개변수 data에 전달된 값을 저장한다.

int LFirst(List *plist, LData * pdata);
- 첫 번째 데이터가 pdata가 가리키는 메모리에 저장한다.
- 데이터의 참조를 위한 초기화가 진행된다.
- 참조 성공 시 TRUE(1), 실패시 FALSE(0) 반환

int LNext(List *plist, LData * pdata);
- 참조된 데이터의 다음 데이터가 pdata가 가리키는 메모리에 저장된다.
- 순차적인 참조를 위해서 반복 호출이 가능하다.
- 참조를 새로 시작하려면 먼저 LFirst 함수를 호출해야 한다.
- 참조 성공 시 TRUE(1), 실패시 FALSE(0) 반환

LData LRemove(List * plist);
- LFirst 또는 LNext 함수의 마지막 반환 데이터를 삭제한다.
- 삭제된 데이터는 반환한다.
- 마지막 반환 데이터를 삭제하므로 연이은 반복 호출을 허용하지 않는다.

int LCount(List * plist);
- 리스트에 저장되어 있는 데이터의 수를 반환한다.
```

LData는 리스트에 저장할 데이터의 자료형에 제한을 두지 않기 위한 typedef 선언의 결과이다.



- 리스트의 ADT를 기반으로 정의한 main 함수



```c
#include <stdio.h>
#include "ArrayList.h"

int main(void){

    // ArrayList의 생성 및 초기화
    List list;
    int data;
    ListInit(&list);

    // 5개의 데이터 저장
    LInsert(&list, 11);
    LInsert(&list, 11);
    LInsert(&list, 22);
    LInsert(&list, 22);
    LInsert(&list, 33);

    // 저장된 데이터의 전체 출력
    printf("현재 데이터의 수 : %d\n", LCount(&list));

    if(LFirst(&list, &data)){ // 첫 번째 데이터 조회
        printf("%d ", data);

        while(LNext(&list, &data)){ // 두 번째 이후 데이터 조회
            printf("%d ", data);
        }
    }
    printf("\n\n");

    // 숫자 22을 탐색해 모두 삭제
    if(LFirst(&list, &data)){
        if(data == 22){
            LRemove(&list);
        }
        while(LNext(&list, &data)){
            if(data == 22){
                LRemove(&list);
            }
        }
    }

    // 삭제 후 남은 데이터 전체 출력
    printf("현재 데이터의 수 : %d\n", LCount(&list));

    if(LFirst(&list, &data)){ // 첫 번째 데이터 조회
        printf("%d ", data);

        while(LNext(&list, &data)){ // 두 번째 이후 데이터 조회
            printf("%d ", data);
        }
    }
    printf("\n\n");
    return 0;

}
```

1. List를 기반으로 변수 list를 선언, 이것을 리스트라 지칭한다.
2. ListInit 함수로 변수의 초기화를 진행한다.
3. LInsert 함수를 호출해 리스트의 주소값을 첫 번째 인자로, 리스트에 담을 데이터를 두 번째 인자로 전달한다.
4. LFirst 함수를 호출해 리스트의 주소값을 첫 번째 인자로, 받아올 첫 데이터를 두 번째 인자로 전달한다.
5. LNext 함수를 호출해 리스트의 주소값을 첫 번째 인자로, 받아올 두 번째 이후의 데이터를 인자로 전달한다.

왜 LFirst 호출이 선행되고, 그 다음 LNext를 호출해야 할까?

LNext 함수는 호출할 때마다 다음에 저장된 데이터를 얻을 수 있는데, 이 기능이 가능한 이유는 데이터의 참조 위치를 기록하기 때문이다. 따라서 처음부터 참조를 시작하려면 이 정보를 초기화해야 한다.

그리고 이를 목적으로 LFirst 함수의 호출을 요구한다.

그렇기 때문에 리스트의 모든 데이터를 참조하려면 함수의 호출 순서를

LFirst -> LNext -> LNext -> LNext ...

와 같이 구성해야 한다.

6. LRemove 함수를 호출해 참조한 데이터 삭제

LRemove 함수가 호출되는 시점은 함수 LFirst 혹은 LNext가 호출된 이후이다. 참조한 데이터를 삭제하는 식인 듯하다.



- 배열을 기반으로 리스트 구현하기1 : 헤더파일의 정의



```c
#ifndef __ARRAY_LIST_H__
#define __ARRAY_LIST_H__

#define TRUE	1 // 참을 표현하기 위한 메크로 정의
#define FALSE	0 // 거짓을 표현하기 위한 메크로 정의

/*** ArrayList의 정의 ****/
#define LIST_LEN	100
typedef int LData;  // LData에 대한 typedef 선언

typedef struct __ArrayList
{
	LData arr[LIST_LEN];
	int numOfData;
	int curPosition;
} ArrayList;


/*** ArrayList와 관련된 연산들 ****/
typedef ArrayList List; // List는 배열 기반 리스트

void ListInit(List * plist); // 초기화
void LInsert(List * plist, LData data); // 데이터 저장

int LFirst(List * plist, LData * pdata); // 첫 데이터 참조
int LNext(List * plist, LData * pdata); // 두 번째 이후 데이터 참조

LData LRemove(List * plist); // 참조한 데이터 삭제
int LCount(List * plist); // 저장된 데이터의 수 반환

#endif
```



- 배열을 기반으로 구현하기2 : 삽입과 조회



```c
#include <stdio.h>
#include "ArrayList.h"

void ListInit(List * plist)
{
	(plist->numOfData) = 0; // 리스트에 저장된 데이터의 수는 0
	(plist->curPosition) = -1; // 현재 아무 위치도 가리키지 않는다.
}

void LInsert(List * plist, LData data)
{
	if(plist->numOfData > LIST_LEN)  // 더 이상 저장할 공간이 없다면
	{
		puts("저장이 불가능합니다.");
		return;
	}

	plist->arr[plist->numOfData] = data;  // 데이터 저장
	(plist->numOfData)++;  // 저장된 데이터 수 증가
}

int LFirst(List * plist, LData * pdata)
{
	if(plist->numOfData == 0) // 저장된 데이터가 하나도 없다면
		return FALSE;

	(plist->curPosition) = 0; // 참조 위치 초기화, 첫 번째 데이터 참조를 의미
	*pdata = plist->arr[0]; // pdata가 가리키는 공간에 데이터 저장
	return TRUE;
}

int LNext(List * plist, LData * pdata)
{
	if(plist->curPosition >= (plist->numOfData)-1) // 더이상 참조할 데이터가 없다면
		return FALSE;

	(plist->curPosition)++;
	*pdata = plist->arr[plist->curPosition];
	return TRUE;
}

LData LRemove(List * plist) // 최근 조회가 이뤄진 데이터를 삭제한다.
{
	int rpos = plist->curPosition; // 삭제할 데이터의 인덱스 값 참조
	int num = plist->numOfData;
	int i;
	LData rdata = plist->arr[rpos];  // 삭제할 데이터를 임시로 저장

	for(i=rpos; i<num-1; i++) // 삭제를 위해 데이터의 이동을 진행
		plist->arr[i] = plist->arr[i+1]; // 빈 공간이 생기니 앞으로 하나씩 당기기

	(plist->numOfData)--; // 데이터 수 감소
	(plist->curPosition)--; // 참조위치를 하나 되돌린다. 참조 인덱스가 삭제되었으니 되돌려야 한다.
	return rdata; // 삭제된 데이터 변환
}

int LCount(List * plist)
{
	return plist->numOfData;
}
```



