#include<stdio.h>

// void disp_meta(char *type, void *dt){
//     printf("Type: %2s, value: %d, size: %lu Bytes\n", type, dt, sizeof(dt));
// }

float calc_incentive(float salary);


int main() {
    // basic data types:
    // int, float, char
    // type modifiers:
    // short, long, signed, unsigned
    // derived types
    // pointer, array, enums, struct
    short unsigned age = 98;
    //negatives are stored as 2's compliment of no
    unsigned int count = 0;
    short comparision = -1;
    float salary=69000.0;
    char typed='y';
    double d=0.2f;

    // storage classes
    // auto, register, static, extern

    // format specifiers
    // %d: [short][signed][unsigned] int
    // %ld-long int

    // disp_meta("Short", age);
    // disp_meta("unsigned int", count);
    // disp_meta("Short signed int", comparision);
    // disp_meta("char", typed);
    printf("Type: %2s, value: %d, size: %lu Bytes\n", "short unsigned", age, sizeof(age));
    printf("Type: %2s, value: %d, size: %lu Bytes\n", "short signed", comparision, sizeof(comparision));
    printf("Type: %2s, value: %d, size: %lu Bytes\n", "unsigned int", count, sizeof(count));
    printf("Type: %2s, value: %d, size: %lu Bytes\n", "char", typed, sizeof(typed));

    printf("Type: %2s, value: %.2f, size: %lu Bytes\n", "float", calc_incentive(salary), sizeof(salary));

    // for(;;){
    //     printf("Yoo!");
    // }

    // while(1){
    //     printf("Yoo!");
    // }

    // do {
    //     printf("Yo!");
    // }while(1);

}

float calc_incentive(float salary){
    float incentive_percentage = 0.2;
    return salary * incentive_percentage;
}
