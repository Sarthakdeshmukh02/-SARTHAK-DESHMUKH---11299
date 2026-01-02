// Q. Write a C program to check whether a number is odd or even.

#include <stdio.h>

int main() {
    int num;

    printf("Enter a number: ");
    scanf("%d", &num);

    if (num % 2 == 0)
        printf("Number is Even");
    else
        printf("Number is Odd");

    return 0;
}