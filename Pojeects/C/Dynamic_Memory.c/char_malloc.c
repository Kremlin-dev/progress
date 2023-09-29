#include <stdio.h>
#include <stdlib.h>

/**
 * main - THis program shows the uses of malloc function to allocate  memory
 * Return: Always 0
*/

int main(void)
{   
    int num,i;
    int *ptr = (int *)malloc(num*sizeof(int));
    
    printf("Please Enter a number of values you want: ");
    scanf("%d", &num);
    if(ptr == NULL)
        exit(1);
    for (i = 0; i < num; i++)
    {
        printf("Please Enter a Value: ");
        scanf("%d", ptr + i);
    }
    for (i = 0; i < num; i++)
    {
        printf("%d\t", *(ptr + i));
    }
    
    return (0);
}