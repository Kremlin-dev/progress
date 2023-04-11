#include <stdio.h>

/**
 * main - Printing addresses and elements in an array using pointers
 * Return: Always zero
*/

int main(void)
{
    int arr[5] = {1,5,7,2,0};
    int i;


for (i = 0; i < 5; i++)
{
    printf("%d\n", &arr[i]);
    printf("%d\t", *(arr + i));
}
    return (0);
}