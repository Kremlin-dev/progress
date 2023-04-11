//In this code, i test my knowledge in multidimensional array
#include <stdio.h>
int main()
{
     int a[2][3] = {1,5,8,4,2,3};
    int i,j;
    for(i=0;i<2;i++){
        for(j=0;j<3;j++){
            printf("%d\t",a[i][j]);
        }
    }
    return 0;
}