#include <stdio.h>
#define SIZE 7

int HasH_T[SIZE];

int hash_fxn(int element)
{
    int key = element % SIZE;
    return (key);
}
void initialize()
{
    int i;
    for (i = 0; i < SIZE; i++)
    {
        HasH_T[i] = 0;
    }
}
void insert(int element)
{
    int key = hash_fxn(element);

    if (HasH_T[key]== 0)
        {
            HasH_T[key] = element;
            printf("Element has been inserted successfully\n");
        }
    else
        {
            printf("Element Already exits.\n");
        }
}

void Print()
{
    int i;
    for (i = 0; i < SIZE; i++)
        {
            printf("HasH_T[%d] = %d\n", i, HasH_T[i]);
        }
}

void delete(int element)
{
    int key = hash_fxn(element);

    if (HasH_T[key]== element)
        {
            HasH_T[key]== -1;
        }
    else
    printf("Element not found in specified location");
}


int main(void)
{
    int num;
    insert(89);
    Print();
    delete(98);
     Print();
}