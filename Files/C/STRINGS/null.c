#include <stdio.h>
#include <string.h>

/**
 * main - prints a string and ends it 
 * Return: 0
*/

int main (void)
{
    char name[4] = {'J','H','O','N'};
    int i;
    for (i = 0; i < 4; i++)
    {
    printf("%c",name[i]);
    }
    return (0);
}