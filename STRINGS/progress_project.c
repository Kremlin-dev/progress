#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX_REG_HOURS 20
#define OVER_TIME_FACTOR 1.5

 /**Reading and writing into a file
This program reads data from a file, calculates regular pay and
over_time pay of workers.
**/
int main(){
// Declaring file pointers and modes
    FILE *in =fopen("name.txt","r");
    FILE *out =fopen("proj.txt","w");
    char firstName[100];
    char lastName[100];
    char name[300];
    int i,hour,rate,regpay,ov_time;
// Using a for loop to write and read from a file
    fprintf(out, "NAME\t\t   HOUR\tRATE  REG_PAY   OV_TIME");
    fprintf(out,"\n\n");
    for(i=0; i<4;i++){
    fscanf(in, "%s",firstName);
    fscanf(in, " %s %d %d",lastName,&hour,&rate);
//Using string functions to copy and concatenate string inputs
    strcpy(name, firstName);
    strcat(name, "  ");
    strcat(name, lastName);
    regpay = rate * hour;
    ov_time = (hour -MAX_REG_HOURS)*rate*regpay;

    fprintf(out, "%s\t %10d %10d %10d %10d",name,hour,rate,regpay,ov_time);
    fprintf(out,"\n");
    }
    fclose(in);
    fclose(out);

    return 0;
}
