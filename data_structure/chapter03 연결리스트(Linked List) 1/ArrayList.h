#include "Point.h"
#ifndef __ARRAY_LIST_H__
#define __ARRAY_LIST_H__

#define TRUE	1 // ���� ǥ���ϱ� ���� ��ũ�� ����
#define FALSE	0 // ������ ǥ���ϱ� ���� ��ũ�� ����

/*** ArrayList�� ���� ****/
#define LIST_LEN	100
// typedef int LData;  // LData�� ���� typedef ����
typedef Point * LData;

typedef struct __ArrayList
{
	LData arr[LIST_LEN];
	int numOfData;
	int curPosition;
} ArrayList;


/*** ArrayList�� ���õ� ����� ****/
typedef ArrayList List; // List�� �迭 ��� ����Ʈ

void ListInit(List * plist); // �ʱ�ȭ
void LInsert(List * plist, LData data); // ������ ����

int LFirst(List * plist, LData * pdata); // ù ������ ����
int LNext(List * plist, LData * pdata); // �� ��° ���� ������ ����

LData LRemove(List * plist); // ������ ������ ����
int LCount(List * plist); // ����� �������� �� ��ȯ

#endif