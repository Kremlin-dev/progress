#include <stdio.h>
#include <string.h>


    

int main(void)
{
char num[11] = "0202108780";
int i;
int sum = 0;

for (i = 0; i < strlen(num); i++)
    {
        num[i];
        printf("%d\t", num[i]);
        sum = 37 + sum + num[i];
    }
     printf("%d\t", sum);
     int index = sum % 256;
      printf("%d\n", index);
}