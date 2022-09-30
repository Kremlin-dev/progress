#include <stdio.h>
#include <stdlib.h>

int main()
{
    FILE *in =fopen("laxer.txt", "w");
    int num;
    char alph = 'y';
    char stri[] = "Hello";
    printf("Enter a value: ");
    scanf("%d",&num);
    fputs(stri, in);
    fputc(alph, in);
    fprintf(in, "%d\n",num);
    fclose(in);

    return 0;
}