#include <stdio.h>
#include <stdlib.h>

int main()
{
 /**This codes takes input of contacts from a user and writes them in a file
    Declaring file pointer
    **/
    FILE *contact = fopen("list.txt","w");
//declaring variables
    char num[100];
    int i;
    
    //using a for loop to take inputs from the user
    for(i=0;i<5;i++)
    {
        //asking for inputs from the user
    printf("Enter a list of contacts to save: ");
//using gets to receive inputs as string from the user
    gets(num);
 //using puts to write into the file
    fputs(num, contact);
    fputs("\n",contact);


    }
//closing the file pointer
    fclose(contact);
    
    return 0;
}