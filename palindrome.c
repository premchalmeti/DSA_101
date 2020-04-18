#include<stdio.h>
#include<string.h>
#include<exstr.h>

int is_palindrome(char* name) {
    int n = strlen(name);
    for(int i=0; i<n/2; i++){
        if(name[i] != name[n-i-1]) {
            return 0;
        }        
    }
    return 1;
}


int main(){
    char *name = "nayan\0", *temp;

    // strcpy(temp, name);
    // strrev(temp);

    // if(strcmp(name, temp)==0) {
    //    printf("%s is palindrome", name);
    // }
    printf("%s is %s\n", name, is_palindrome(name)?"Palindrome": "not Palindrome");

    return 0;
}
