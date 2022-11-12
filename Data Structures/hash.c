#include <stdio.h>
#include <string.h>



int main(void)
{
char num[11] = "0244278257";

int i; 
int sum = 0;
for(i = 0; i <= strlen(num); i++)
{
    sum = sum+ num[i];
    printf("%c\t", num[i]);
}
printf("%d\n", sum);
}