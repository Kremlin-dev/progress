#include <stdio.h>
#include <string.h>
#define SIZE 256

struct contact
{
    char *key;
    char *value;
};
struct contact num[SIZE];
int Hash_fxn(char *key);
void initial()
{
    for (int i = 0; i < SIZE; i++)
  {
  num[i].key = 0;
  num[i].value = 0;
   printf("%d %d",  num[i].key,num[i].value);
  }  
  //printf("Key at: %d\n",  num[154].key);  
}

void Add_item(char *key, char *value)
 {
    int i = Hash_fxn(key);
    if (num[i].value == 0 )
        {
            num[i].key = key;
            num[i].value = value;  
            printf(" %s %s \n", num[i].key,num[i].value);
        }
        else
        {

            printf("Name Exits on the List.\n");
        }    

 }

 int Hash_fxn(char *key)
 {
     int i,sum = 0;
   for (i = 0; i < strlen(key); i++)
    {
        sum = 37 + sum + key[i];
    }
     int index = sum % SIZE;
     return (index);
}

int main(void)
{
    //initial();
    Add_item("Isaac", "0244278257");
    Add_item("yaw", "0244278257");
    Add_item("Isaac", "0244278257");
    //Hash_fxn("Isaac");
    

}
 