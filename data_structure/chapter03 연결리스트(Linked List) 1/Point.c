#include <stdio.h>
#include "Point.h"

// Point 변수의 xpos, ypos 값 설정
void SetPointPos(Point * ppos, int xpos, int ypos){
    ppos->xpos = xpos;
    ppos->ypos = ypos;
}

// Point 변수의 xpos, ypos 정보 출력
void ShowPointPos(Point * ppos){
    printf("[%d, %d] \n", ppos->xpos, ppos->ypos);
}

// 두 Point 변수의 비교
int PointComp(Point * pos1, Point * pos2){
    if(pos1->xpos == pos2->xpos && pos1->ypos == pos2->ypos){
        return 0;
    }else if(pos1->xpos == pos2->xpos){
        return 1;
    }else if(pos1->ypos == pos2->ypos){
        return 2;
    }else{
        return -1;
    }
}