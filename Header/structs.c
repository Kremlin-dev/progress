#include <stdio.h>
#include <string.h>

 struct student
    {
        char name[20];
        int age;
        char id[10];
        int grade;
    };

    /**
     *  main - Struct basics implementation
     * Return: Always 0
    */

int main(void)
{
    struct student Isaac;
    
    strcpy(Isaac.name, "Isaac Amponsah");
    strcpy(Isaac.id, "03121450");
    Isaac.age = 22;
    Isaac.grade = 80;
    printf("Student Details\n");
    printf("Name: %s\n",Isaac.name);
    printf("Age: %d\n",Isaac.age);
    printf("Student's ID: %s\n",Isaac.id);
    printf("Grade: %d\n",Isaac.grade);    
    return (0);
}