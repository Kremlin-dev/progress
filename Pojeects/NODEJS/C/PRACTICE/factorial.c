#include <stdio.h>
#include <stdlib.h>
int main(){
    int factorial=1, n,h;
    printf("Enter a value: ");
    scanf("%d",&n);
    
    for(h =2;h<=n;h++)
    {
        factorial = factorial * h;
    }
    
    printf("%d!= %d ",n,factorial);
    return 0;
}