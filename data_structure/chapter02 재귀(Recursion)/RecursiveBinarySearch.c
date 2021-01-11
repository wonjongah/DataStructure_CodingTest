#include <stdio.h>

int BSearchRecur(int ar[], int first, int last, int target){

    int mid;

    if(first > last){
        return -1;
    }
    mid = (first + last) / 2;

    if(ar[mid] == target){
        return mid;
    }else if(target < ar[mid]){ // Å¸°ÙÀÌ Áß°£°ªº¸´Ù ÀÛÀ¸¸é, last¸¦ mid - 1·Î ÁöÁ¤ÇÏ°í ´Ù½Ã Å½»ö
        return BSearchRecur(ar, first, mid-1, target);
    }else{ // Å¸°ÙÀÌ Áß°£°ªº¸´Ù Å©¸é first¸¦ mid + 1·Î ÁöÁ¤ÇÏ°í ´Ù½Ã Å½»ö
        return BSearchRecur(ar, mid + 1, last, target);
    }
}

int main(void){

    int arr[] = {1,3,5,7,9};
    int idx;

    idx = BSearchRecur(arr, 0, sizeof(arr)/sizeof(int)-1, 7);
    if(idx == -1){
        printf("Å½»ö ½ÇÆÐ \n");
    }else{
        printf("Å¸°Ù ÀúÀå ÀÎµ¦½º: %d \n", idx);
    }

    idx = BSearchRecur(arr, 0, sizeof(arr)/sizeof(int)-1, 4);
    if(idx == -1){
        printf("Å½»ö ½ÇÆÐ \n");
    }else{
        printf("Å¸°Ù ÀúÀå ÀÎµ¦½º: %d \n", idx);
    }
    }