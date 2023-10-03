#include <stdio.h>
int main(void)
{
    int i,j,sum =0;
    int arr[2][2] = {{1,3},{4,5}};
    for(i=0;i<2;i++){
        for(j=0;j<2;j++){
            //printf("%d\n",arr[i][j]);
            sum = sum +arr[i][j];
        }
        printf("%d\t",sum);
        sum =0;
    }
    for(j=0;j<2;j++){
        for(i=0;i<2;i++){
            //printf("%d\n",arr[i][j]);
            sum = sum +arr[i][j];
        }
        printf("%d\t",sum);
        sum =0;
    }

    return (0);
}