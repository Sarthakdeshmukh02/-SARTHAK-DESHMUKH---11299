// Q. Write a C program to demonstrate the use of both break and continue in a single loop.

#include <stdio.h>

int main() {
    int i;

    for (i = 1; i <= 10; i++) {

        if (i == 3)
            continue;   // 3 skip hoga

        if (i == 7)
            break;      // loop yahin end ho jaayega

        printf("%d ", i);
    }

    return 0;
}