#include  <stdio.h>
#include <stdlib.h>
//This programs is to illustrate basic operations of characters in C

int main()

{

   int ch;
   float c = 12.45698;
   /**
   printf("Enter a character: ");
   //when you use getc to take input from the user stdin must be present
   //ch =getc(stdin);
   ch =getchar();
    printf("The character you input was %c\n",ch);
    
   printf("%20f\n",c); 
    printf("%.3f",c);

   int x=2,y=6;
   printf("x<=y is: %d\n",x<=y);
   printf("Float value of x is : %f",(float)x);

  int size = sizeof(double);
  printf("%d",size);
  **/

 int x=8,y =2;
 int z;
 z = x>>y;
 printf("%d",z);

    return 0;   

}