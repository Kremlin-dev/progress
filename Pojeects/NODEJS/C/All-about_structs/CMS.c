#include <stdio.h>
#include <stdlib.h>
#define SIZE 256

struct contact
{
    int key;
    int value;
};
struct contact num[SIZE];
void initial()
{
    for (int i = 0; i < SIZE; i++)
  {
  num[i].key = 0;
  num[i].value = 0;
  }    
}
 int hashfxn(char *key)
 {
     int index;
   for (i = 0; i < strlen(num); i++)
    {
        sum = 37 + sum + num[i];
    }
     printf("%d\t", sum);
     int index = sum % 256;
      printf("%d\n", index);
}
 

 void insert(int key, int value)
 {
    int index = hashfxn(key);
    if (num[index].value == 0)
        {
            num[index].key = index; // Need to look at it
            num[index].value = value;
            printf("%d %d", num[index],num[index].value);
        }
 }

 int main()
 {
     
     insert(300, 98);
 }
