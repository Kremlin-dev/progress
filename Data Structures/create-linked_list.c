#include <stdio.h>
#include <stdlib.h>

/**
 * main -creeates the node of a linked list
 * 
 * Return: Always 0
*/

struct node 
{
    int data;
    struct node *link;
};

int main(void)
{   
    struct node *head = malloc(sizeof(struct node));
    head ->data = 12;
    head ->link = NULL;

    printf("%d\t", head ->data);

    struct node *current = malloc(sizeof(struct node));
    current  ->data = 56;
    current->link = NULL;
    head ->link = current;

     printf("%d", current ->data);


    return (0);
}