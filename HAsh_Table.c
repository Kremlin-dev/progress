#include <stdio.h>
#include <stdlib.h>

#define SIZE 40

int hash_fxn(int element)
{
    int key = element % SIZE;
    return (key);
}
int main(void)
{
int *Hash_t = malloc(SIZE * sizeof(int))
}
