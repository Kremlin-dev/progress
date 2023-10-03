#include <stdio.h>
#include <stdlib.h>
//This code reads integer data from a file
int main(){
// Declaring a file pointer
    FILE *out =fopen("read.txt","r");
//Declaring variables
  int num;
// Using fscanf to read from the file and printing out to the screen
fscanf(out, "%d",&num);
printf("%d",num);
fclose(out);
    
    return 0;
}