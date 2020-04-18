// Aim: calculate 6 types of lucky numbers based on full name and DOB
// reference: https://en.wikibooks.org/wiki/C_Programming/String_manipulation
// naming conventions: https://www.doc.ic.ac.uk/lab/cplus/cstyle.html

#include<stdio.h>
#include<string.h>


char* get_firstname(char* fullname){
    
}

int main() {
    char fullname[50] = "Premkumar Ashok Chalmeti\0";
    char first_name[5] = {'P', 'r', 'e', 'm', '\0'};
    char greeting[] = "Hey %s! How are you?\n";
    
    // printf("Hey %s! How are you?\n", first_name);
    
    printf(greeting, first_name);
    printf("Fullname: %s\n", fullname);
        
    return 0;
}
