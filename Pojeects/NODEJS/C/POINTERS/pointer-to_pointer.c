#include <stdio.h>

/**
 * main - checks the address of a pointer to a pointer
 * Return: Always 0
*/

int main(void)
{
    int age = 6;
    int *p;
    p = &age;

    int **q;
    q = &p;

    printf("%d\t",age);
    printf("%p\t",&age);
    printf("%d\t",*p);
    printf("%d\t",&p);
    printf("%d\t",q);


    return (0);
}