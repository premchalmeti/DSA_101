#include<stdio.h>
#define MAX 9999

int get_arr_len(int *arr){
    return sizeof(arr)/sizeof(arr[0]);
}


int main(){
    int arr[] = {1,2,3};
    printf("%d", get_arr_len(arr));
    return 0;
}
