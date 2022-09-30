#include <stdio.h>
#include <stdlib.h>

int main()
{
    FILE *pint = fopen("file.txt","w");
    int number[20];
    printf("Enter a phone number: ");
    scanf("%s",&number);
    fputs(number,pint);
    fclose(pint);
    return 0;
}