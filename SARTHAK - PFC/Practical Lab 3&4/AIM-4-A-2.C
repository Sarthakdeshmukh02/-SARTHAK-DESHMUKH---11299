// Q2(a). Example to show use of return in a function.

#include <stdio.h>

int add(int a, int b) {
    return a + b;
}

int main() {
    int sum = add(5, 3);
    printf("Sum = %d", sum);
    return 0;
}