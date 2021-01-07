#include <stdio.h>

int BSearch(int ar[], int len, int target){
    int first = 0; // Ω√¿€ ¿Œµ¶Ω∫
    int last = len - 1;
    int mid;

    while(first <= last){
        mid = (first + last) / 2; // ≈Ωªˆ ¥ÎªÛ¿« ¡ﬂæ” ¿Œµ¶Ω∫

        if(target == ar[mid]){ // ¡ﬂæ”¿« ∞™¿Ã ≈∏∞Ÿ∞™¿Ã∂Û∏È
            return mid;  // ¿Œµ¶Ω∫ ∞™ ∏Æ≈œ«œ∞Ì ≈Ωªˆ ¡æ∑·!
        }
        else{
            if(target < ar[mid]){
                last = mid - 1; 
            }
            else{
                first = mid + 1;
            }
        }
    }
    return -1; // √£¡ˆ ∏¯«ﬂ¿ª ∂ß π›»Øµ«¥¬ ∞™ -1
}

int main(void){
    int arr[] = {1,3,5,7,9};
    int idx;

    idx = BSearch(arr, sizeof(arr)/sizeof(int), 7);
    if(idx == -1){
        printf("≈Ωªˆ Ω«∆– \n");
    }else{
        printf("≈∏∞Ÿ ¿˙¿Â ¿Œµ¶Ω∫ : %d \n", idx);
    }

    idx = BSearch(arr, sizeof(arr)/sizeof(int), 4);
    if(idx == -1){
        printf("≈Ωªˆ Ω«∆– \n");
    }else{
        printf("≈∏∞Ÿ ¿˙¿Â ¿Œµ¶Ω∫ : %d \n", idx);
    }

    return 0;
}