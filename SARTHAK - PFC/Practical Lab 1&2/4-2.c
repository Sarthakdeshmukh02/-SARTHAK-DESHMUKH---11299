// Q. Write a C program to find the largest of two numbers using ternary operator.

#include <stdio.h>

int main() {
    int a, b;

    printf("Enter two numbers: ");
    scanf("%d %d", &a, &b);

    (a > b) ? printf("%d is largest", a) : printf("%d is largest", b);

    return 0;
}