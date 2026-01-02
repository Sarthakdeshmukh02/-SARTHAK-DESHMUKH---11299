#include <stdio.h>

int main()
{
    int a;
    float b;
    char c;
    double d;

    printf("Enter an integer, float, character, and double value:\n");
    scanf("%d %f %c %lf", &a, &b, &c, &d);

    printf("\nYou entered:\n");
    printf("Integer: %d\n", a);
    printf("Float: %.2f\n", b);
    printf("Character: %c\n", c);
    printf("Double: %.3lf\n", d);

    // Swapping two numbers
    int x, y, temp;
    printf("\nEnter two numbers to swap: ");
    scanf("%d %d", &x, &y);
    temp = x;
    x = y;
    y = temp;
    printf("After swapping: x = %d, y = %d\n", x, y);

    return 0;
}
