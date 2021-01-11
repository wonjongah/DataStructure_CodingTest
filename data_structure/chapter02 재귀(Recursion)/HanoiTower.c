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