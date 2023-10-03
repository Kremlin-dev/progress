#include <stdio.h>
#include <stdlib.h>




int sun(int *m)
    {
        for (int i = 0; i < m; i++) 
    {
	    if  (s[i] >= '0' && s[i] <= '9')
            {
                sum = sum +  atoi(argv[i]);

            }
    }
/**
  * main - Adds positive integers

  *@argc: Argument counter

  *@argv: Arguement vector

  * Return: Always 0

  */
int main(int argc, char **argv)
{

int i;

int sum = 0;

if (argc <= 2)
    {
    printf("%d", 0);
    }

    else
    {
        for (i = 0; i < argc; i++)
            {
                if (atoi(argv[i]) > 0 )
                    {
                    sum = sum +  atoi(argv[i]);
                    } 
            }
             printf("%d\n", sum);
            
                    //printf("shit\n");

            
    }
    return (0);
}