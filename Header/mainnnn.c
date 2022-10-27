#include <stdio.h>

int main(void)
{
   int i;

   for (i =1; i <= 10; i++)
   {
       if (i % 2 != 0)
       {
              printf("%d\t", i+1);
       }
       else if (i % 2 == 0)
       {
               printf("%d\t", i-1);
       }
       else 
       printf("%d\t",i);
   }
   
    
       }


