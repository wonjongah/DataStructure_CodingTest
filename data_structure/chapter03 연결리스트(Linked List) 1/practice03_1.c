#include <stdio.h>
#include "ArrayList.h"

int main(void){

    // ArrayList의 생성 및 초기화
    List list;
    int data;
    ListInit(&list);

    // 1~9까지 데이터 저장
    for(int i = 1; i < 10; i++){
        LInsert(&list, i);
    }

    printf("현재 데이터의 수 : %d\n", LCount(&list));

    // 저장된 데이터의 전체 합 출력
    int sum = 0;
    
    if(LFirst(&list, &data)){ // 첫 번째 데이터 조회
        sum += data;

        while(LNext(&list, &data)){ // 두 번째 이후 데이터 조회
            sum += data;
        }
    }
    printf("전체 데이터의 합 : %d\n", sum);

    // 2의 배수와 3의 배수를 탐색해 모두 삭제
    if(LFirst(&list, &data)){
        if(data % 2 == 0 || data % 3 == 0){
            LRemove(&list);
        }
        while(LNext(&list, &data)){
            if(data % 2 == 0 || data % 3 == 0){
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
    printf("\n");
    return 0;

}