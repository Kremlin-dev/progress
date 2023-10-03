#include <stdio.h>
#include <stdlib.h>

int main()
{
    int x=8;
    int *y;
    y = &x;
    printf("%p\n",y);
    printf("%d",*y);
    return 0;
}
