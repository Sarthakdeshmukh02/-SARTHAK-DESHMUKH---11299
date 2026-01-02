// Q. Write a C program to calculate the sum of first N natural numbers using any loop.

#include <stdio.h>

int main() {
    int n, i, sum = 0;

    printf("Enter value of N: ");
    scanf("%d", &n);

    for (i = 1; i <= n; i++) {
        sum = sum + i;
    }

    printf("Sum = %d", sum);

    return 0;
}