#include <stdio.h>
int main(){
    //Program to print scores in an array using a for loop
    int score[60]; //Declaring variables
    int h;
    //using a for loop to print out score
    for(h=0; h<20;h++){
        score[h]=2;
        printf("%d\t",score[h]);
    }
    return 0;
}