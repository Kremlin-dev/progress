#include <stdio.h>
#include <stdlib.h>
#include <string.h>


char *str_concat(char *s1, char *s2)
{
    int i, j;
    char *ptr = malloc(i * sizeof(char));

    for (i = 0; *s1 != '\0';)
        {
            ptr[j] = s1[i];
            i++;
            j++;
        }
    for (j = 0; *ptr != '\0';)
        {
            ptr[j] = + s2[i];
            i++;
            j++;
            
        }
     return (ptr);

}   

int main(void)
{
    char *s;

    s = str_concat("Betty ", "Holberton");
    if (s == NULL)
    {
        printf("failed\n");
        return (1);
    }
    printf("%s\n", s);
    free(s);
    return (0);
}

