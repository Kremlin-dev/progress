#include <stdio.h>
/**
 * main - Passing arrays to functions
 * Return: Always 0
*/

int summation(int B[], int size);

int main(void)
{
int A[5] = {3,6,8,1,4};
int total, size;

size = sizeof(A) / sizeof(A[0]);
total = summation(A, size);
printf("%d",total);
    return (0);
}

/**
 * summation - Calculates the sum of an array
 * Return: sum
*/

int summation(int B[], int size)
{
    int sum = 0;
    int i;


    for (i = 0; i < size; i++)
    {
        sum += B[i];
    }
    return (sum);
    
}