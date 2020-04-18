#include<stdio.h>

// using namespace std;
// Todo: Conver this program to OOP using shapes as base class

float area(short radius){
    return 2 * 3.14 * radius * radius;
}

float perimeter(short radius){
    return 2 * 3.14 * radius;
}


int main() {
    short radius=0;

    // cout<<"Radius of circle: %d"<<radius;
    printf("Enter radius of circle:");
    scanf("%hd", &radius);
    printf("Area: %f\nPerimeter: %f\n", area(radius), perimeter(radius));
    return 0;
}
