#include <stdio.h>
#include <stdlib.h>
#define SIZE 256

int Hash_t[SIZE];

int hash_fxn(int element)
{
    int key = ((element % SIZE) % 10);
    return (key);
}
void initialize()
{
    int i;
    for (i = 0; i < SIZE; i++)
    {
        Hash_t[i] = 0;
    }
}
void insert(int element)
{
    int key = hash_fxn(element);

    if (Hash_t[key]== 0)
        {
            Hash_t[key] = element;
            printf("Element has been inserted successfully\n");
        }
    else
        {
            printf("Element Already exits.\n");
        }
}

void delete(int element)
{
    int key = hash_fxn(element);

    if (Hash_t[key]== element)
        {
            Hash_t[key] = 0;
        }
    else
    printf("Element not found in specified location");
}
void Print()
{
    int i;
    for (i = 0; i < SIZE; i++)
        { if (Hash_t[i] != 0)
            {
            printf("Hash_t[%d] = %d\n", i, Hash_t[i]);
           }
       }
}

int main(void)
{
    int Choice, num;
    printf("//////////////////////////////////////////////\n");

    menu:
    printf("1. Insert Element \n");
    printf("2. Delete Element \n");
    printf("3. Print List \n");

    printf("Enter Choice: ",Choice);
    scanf("%d",&Choice);


    switch(Choice)
    {
        //Case 1 to initiate a withdrawal process.
        case 1 :
        printf("Enter a value to insert: ");
        scanf("%d",&num);
        insert(num);
        goto menu;
        break;

        case 2:
        printf("Enter a value to delete: ");
        scanf("%d",&num);
        delete(num);
        goto menu;
        break;

        case 3:
        Print();
        goto menu;
    }
}
