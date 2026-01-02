// Q1. Write a function that returns the square of a number.

#include <stdio.h>

int square(int n) {
    return n * n;
}

int main() {
    int num;

    printf("Enter a number: ");
    scanf("%d", &num);

    printf("Square = %d", square(num));

    return 0;
}