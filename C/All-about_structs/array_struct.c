#include <stdio.h>

struct student
{
   
    char name[20]; 
    char id[6];
    int marks;
    
};

int main(void)
{
    struct student per[2];
    int i;
    for (i = 0; i < 2; i++)
        {
            printf("Enter your name: ", i + 1);
            scanf("%s", per[i].name);

            printf("Enter your ID: ",i + 1);
            scanf("%s", per[i].id);

            printf("Enter your marks: ",i + 1);
            scanf("%d", &per[i].marks);
           
        }
      
    for (i = 0; i < 2; i++)
        {
            printf("%s %s %d", per[i].name,per[i].id, per[i].marks);
            printf("\t");

        }
       
}

