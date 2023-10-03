#include <stdio.h>
#include <stdlib.h>



char *str_concat(char *s1, char *s2)
{
    int i,j;
 char *s3 = malloc(50 * sizeof(char));

    while (s1[i] != '\0') 
    {
        s3[j] = s1[i];
        i++;
        j++;
    }
    i = 0;
    while (s2[i] != '\0')
     {
        s3[j] = s2[i];
        i++;
        j++;
    }
    s3[j] = '\0';
    return (s3++);
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


