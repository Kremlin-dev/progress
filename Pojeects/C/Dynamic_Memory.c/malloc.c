#include <stdio.h>
#include <stdlib.h>

/**
 * main - THis program shows the uses of malloc function to allocate  memory
 * Return: Always 0
*/

int main(void)
{   
    int *ptr = (int *)malloc(4);
    
    printf("Please Enter a value: ");
    scanf("%d",ptr);
    printf("%d",*ptr);
    
    return (0);
}