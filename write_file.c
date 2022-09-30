#include <stdio.h>
#include <stdlib.h>

int main()
{
    FILE *pint = fopen("file.txt","w");
    int number;
    printf("Enter a phone number: ");
    scanf("%d",&number);
    fprintf(pint, "%d",number);
    fclose(pint);
    return 0;
}