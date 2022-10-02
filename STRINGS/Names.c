#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
    FILE *in =fopen("name.txt","r");
    char firstName[20];
    char lastName[20];
    char name[40];
    int i;
    for(i=0; i<2;i++){

    fscanf(in, "%s",firstName);
    strcpy(name, firstName);
    strcat(name, " ");
    fscanf(in, "%s",lastName);
    strcat(name, lastName);
    printf("%s\n",name);
    }
    fclose(in);
    
    return 0;
}