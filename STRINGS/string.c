#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//This code revises string functions i.e strcat

int main(){
// Declaring variables
    char first[20];
    char last[10];
    char var_1[20] = "C programming";
    char var_2[20];
// Taking inputs from the user
    printf("Enter your first name: ");
    scanf("%s",&first);
    printf("Enter your last name: ");
    scanf("%s",&last);
// Using the string functiom to concatenate 
    strcat(first, " " );
    strcat(first, last);
    printf("%s\n",first);
//Using strcpy to copy strings
    strcpy(var_2, var_1);
    printf("%s\n",var_2);
    return 0;
}