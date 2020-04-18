#include<stdio.h>


int main() {
    short i = 20;
    short *i_ptr = &i;
    short **ii_ptr = &i_ptr;

    printf("Value is %d, address is %u\n", i, &i);
    printf("Using ptr, Value is %d, Address is %u\n", *i_ptr, i_ptr);

    printf("Using dbl ptr value is %d\n", **ii_ptr);

    return 0;
}
