// Q. Write a C program to find the maximum of three numbers using nested if.

#include <stdio.h>

int main() {
    int a, b, c;

    printf("Enter three numbers: ");
    scanf("%d %d %d", &a, &b, &c);

    if (a > b) {
        if (a > c)
            printf("%d is the maximum", a);
        else
            printf("%d is the maximum", c);
    } else {
        if (b > c)
            printf("%d is the maximum", b);
        else
            printf("%d is the maximum", c);
    }

    return 0;
}