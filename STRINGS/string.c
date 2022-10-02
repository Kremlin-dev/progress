#include <stdio.h>
#include <stdlib.h>
#include <string.h>
//This code revises string functions i.e strcat

int main(){
// Declaring variables
    char first[20];
    char last[10];
// Taking inputs from the user
    printf("Enter your first name: ");
    scanf("%s",&first);
    printf("Enter your last name: ");
    scanf("%s",&last);
// Usinfg the string functiom to concatenate 
    strcat(first, " " );
    strcat(first, last);
    printf("%s",first);
    return 0;
}