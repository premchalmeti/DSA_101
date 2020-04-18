#include<stdio.h>

int fact(short no) {
    return no == 1? 1: no * fact(no - 1);
}

int main(int argc, int *argv[]) {
    // short no = argc==2? 5: *argv[1];
    // printf("%d, %d", argc, (int) *argv[0]);
    printf("%d = %d\n", 5, fact(5));
    return 0;
}
