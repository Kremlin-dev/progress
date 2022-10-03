#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// Reading and writing into a file
int main(){
// Declaring file pointers and modes
    FILE *in =fopen("name.txt","r");
    FILE *out =fopen("proj.txt","w");
    char firstName[100];
    char lastName[100];
    char name[300];
    int i,hour;
    int rate;
// Using a for loop to write and read from a file

    for(i=0; i<4;i++){
    fscanf(in, "%s",firstName);
    fscanf(in, " %s %d %d",lastName,&hour,&rate);
    strcpy(name, firstName);
    strcat(name, "  ");
    strcat(name, lastName);
    fprintf(out, "%s\t %10d %10d",name,hour,rate);
    fprintf(out,"\n");
    //fprintf(out, "%5d",hour);
    }
    fclose(in);
    fclose(out);


    return 0;
}
