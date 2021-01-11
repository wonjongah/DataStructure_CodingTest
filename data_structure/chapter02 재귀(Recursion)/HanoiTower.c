#include <stdio.h>

void HanoiTowerMove(int num, char from, char by, char to){
    // from�� �����ִ� num���� ������ by�� ���ļ� to�� �̵�

    if(num == 1)  // �̵��� ������ ���� 1�����, Ż�� ����
    {
        printf("����1�� %c���� %c�� �̵� \n", from, to);
    }else{
        HanoiTowerMove(num-1, from, to, by); // 3�ܰ� �� 1�ܰ�
        // n-1���� ������ A���� B��
        printf("����%d�� %c���� %c�� �̵� \n", num, from, to); // 3�ܰ� �� 2�ܰ�
        // ������ ������ A���� C��
        HanoiTowerMove(num-1, by, from, to);  // 3�ܰ� �� 3�ܰ�
        // n-1���� ������ B���� C��
    }
}

int main(void){
    // ����A�� ���� 3���� ���� B�� �����Ͽ� ���� C�� �ű��
    HanoiTowerMove(3, 'A', 'B', 'C');
    return 0;
}