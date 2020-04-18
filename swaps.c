#include<stdio.h>


void swap(int *n1, int *n2) { 
    int t = *n1;
    *n1 = *n2;
    *n2 = t;
}

int main(){
    int n1 = 10, n2 = 20;


    printf("%d, %d\n", n1, n2);
    
    swap(&n1, &n2);

    printf("%d, %d\n", n1, n2);
    return 0;
}
