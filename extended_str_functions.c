#include<stdio.h>
#include<string.h>

void swap(char *c1, char *c2){
    char temp = *c1;
    *c1 = *c2;
    *c2 = temp;
}


void strrev(char* src) {
    int n = strlen(src);
    for(int i=0; i<n/2; i++) {
        swap(&src[i], &src[n-i-1]);
    }
}


int main() {
    char fullname[50], temp[50];
    // fgets(fullname, 50, stdin);
    scanf("%s", fullname);
    strcpy(temp, fullname);
    strrev(temp);
    printf("strrev(%s) = %s\n", fullname, temp);
    return 0;
}

