#include <stdio.h>
#include <string.h>

/**
 * _strcat - Concatenates two strings
 * @dest: pointer arguement
 * @src: pointer arguement
 * Return: String
*/

char *_strcat(char *dest, char *src)
{   int i,j;
    for (i = 0; dest[i] != '\0';)
    {
        i++;

    }
    for (j = 0; src[j] != '\0';)
    {
        dest[i] = src[j];
        j++;
        i++;

    }
    return (dest);
}

#include <stdio.h>

/**
 * main - check the code
 *
 * Return: Always 0.
 */
int main(void)
{
    char s1[98] = "Hello ";
    char s2[] = "World!\n";
    char *ptr;

    printf("%s\n", s1);
    printf("%s", s2);
    ptr = _strcat(s1, s2);
    printf("%s", s1);
    printf("%s", s2);
    printf("%s", ptr);
    return (0);
}