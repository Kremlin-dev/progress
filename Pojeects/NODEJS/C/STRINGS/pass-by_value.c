//This program receives two values from a user and swaps them by passing by reference
#include <stdio.h>
//Void function prototype with pointer arguments
int change(int x,int y);

int main (){
    int m = 10,n =20;
    change(m,n);
 
    return 0;
}
//function definition
int change(int x,int y)
{
    int temp = x;
    x = y;
    y = temp;
     printf("%d %d",x,y);
    
}
