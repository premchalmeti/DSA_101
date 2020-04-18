#include<stdio.h>
#include<math.h>


int square(int no) {
    return no * no;
}

int cube(int no) {
    return no * no * no;
}

void swap(short *n1, short *n2) {
    int aux = 0;
    aux = *n1;
    *n1 = *n2;
    *n2 = aux;
}


int main() {
    short no1=3, no2=2;

    scanf("%hd %hd", &no1, &no2);
    printf("No %d's, square is %d, cube is %d\n", no1, square(no1), cube(no1));

    swap(&no1, &no2);

    printf("Swapped %d, %d\n", no1, no2);

    return 0;
}
