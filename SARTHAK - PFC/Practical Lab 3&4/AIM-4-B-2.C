// Q2(b). Example to show use of printf inside a function.

#include <stdio.h>

void add(int a, int b) {
    printf("Sum = %d", a + b);
}

int main() {
    add(5, 3);
    return 0;
}