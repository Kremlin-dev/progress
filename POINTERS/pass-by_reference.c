//This program receives two values from a user and swaps them by passing by reference
#include <stdio.h>
//Void function declaration with pointer arguments
void change(int *x,int *y);

int main (){
    int m = 10,n =20;
    change(&m,&n);
    printf("%d %d",m,n);
    return 0;

}
//function
void change(int *x,int *y)
{
    int temp = *x;
    *x = *y;
    *y = temp;
}
