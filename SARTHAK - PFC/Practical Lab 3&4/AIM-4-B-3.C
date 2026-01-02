// Q3(b). Write a function to find factorial of a number.

#include <stdio.h>

int factorial(int n) {
    int i, fact = 1;
    for (i = 1; i <= n; i++) {
        fact = fact * i;
    }
    return fact;
}

int main() {
    int num;
    scanf("%d", &num);

    printf("Factorial = %d", factorial(num));

    return 0;
}