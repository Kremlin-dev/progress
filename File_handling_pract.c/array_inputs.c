#include <stdio.h>
#include <stdlib.h>

int main()
{
    FILE *Phone_Numbers = fopen("book.txt","w");
    char *number[100] = {"0558507341","0244278257","0244260141","0208935384","0202108780"};
    int i;
    for(i=0;i<5;i++)
    {
    fprintf(Phone_Numbers, "%s\n",number[i]);
    }
    fclose(Phone_Numbers);
    return 0;
}