/*
    Aim: calculate 6 types of lucky numbers based on full name and DOB
    reference: https://www.wikihow.com/Find-Your-Lucky-Numbers-in-Numerology
    naming conventions: https://www.doc.ic.ac.uk/lab/cplus/cstyle.html
*/


#include<stdio.h>
#include<string.h>

#define FULL_NAME_LIMIT 64
#define DOB_LIMIT 11

void strstrip(char *source){
    // strcspn() return index of another string in first
    source[strcspn(source, "\n")] = '\0';
}

/*char* get_firstname(char *fullname){
    return strsplit(fullname);
}*/

int parse_dob(char *dob){
    int day=0, month=0, year=0;

    for(int i=0; i<strlen(dob); i++){
        if(dob[i] == '/')
        day = dob[i];
    }
}

void calc_lucky_numbers(char *dob, int* lucky_numbers){
    // calculcate 6 lucky numbers and return in array
    // 1. Life path number
    lucky_numbers[0] = 12;
    
}


int main() {
    char fullname[FULL_NAME_LIMIT];
    char dob[DOB_LIMIT];
    int lucky_numbers[6] = {};
    printf("What's your full name<fname mname lname>?\n>>");
    // gets() no bounds checking, no boundry checks
    // fgets() reads given limit string
    fgets(fullname, FULL_NAME_LIMIT, stdin);

    strstrip(fullname);

    printf("Hey %s, Please tell us your Birthdate<dd/mm/yyyy>?\n>>", fullname);
    fgets(dob, DOB_LIMIT, stdin);

    strstrip(dob);

    calc_lucky_numbers(dob, lucky_numbers);

    printf("%s\n%s\n", fullname, dob);


    printf("Your lucky numbers are, \n%d\n", lucky_numbers[0]);

    return 0;
}
