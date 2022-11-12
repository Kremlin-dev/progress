#include <stdio.h>

#include <stdio.h>

struct student
{
    char name[20]; 
    char id[6];
    int marks;  
};

int main(void)
{
    struct student per = {"Isaac", "2023120", 45};
    struct student *ptr = &per;

    printf("%s %s %d", ptr -> name, ptr -> id, ptr -> marks);
  
}