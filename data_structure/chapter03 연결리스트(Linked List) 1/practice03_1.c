#include <stdio.h>
#include "ArrayList.h"

int main(void){

    // ArrayList�� ���� �� �ʱ�ȭ
    List list;
    int data;
    ListInit(&list);

    // 1~9���� ������ ����
    for(int i = 1; i < 10; i++){
        LInsert(&list, i);
    }

    printf("���� �������� �� : %d\n", LCount(&list));

    // ����� �������� ��ü �� ���
    int sum = 0;
    
    if(LFirst(&list, &data)){ // ù ��° ������ ��ȸ
        sum += data;

        while(LNext(&list, &data)){ // �� ��° ���� ������ ��ȸ
            sum += data;
        }
    }
    printf("��ü �������� �� : %d\n", sum);

    // 2�� ����� 3�� ����� Ž���� ��� ����
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

    // ���� �� ���� ������ ��ü ���
    printf("���� �������� �� : %d\n", LCount(&list));

    if(LFirst(&list, &data)){ // ù ��° ������ ��ȸ
        printf("%d ", data);

        while(LNext(&list, &data)){ // �� ��° ���� ������ ��ȸ
            printf("%d ", data);
        }
    }
    printf("\n");
    return 0;

}