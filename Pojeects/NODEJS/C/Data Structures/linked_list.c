#include <stdio.h>
#include <stdlib.h>

struct node
{
    int data;
    struct node *link;
};

int main(void)
{
    struct node *head = NULL;

    head = malloc(sizeof(struct node));
    head -> data = 45;
    head ->link = NULL;

    struct node *current = NULL;
    current = malloc(sizeof(struct node));
    current -> data = 98;
    current ->link = NULL;
    head ->link = current;

    struct node *next = NULL;
    next = malloc(sizeof(struct node));
    next -> data = 3;
    next ->link = NULL;
    current ->link = next;


    printf("%d\t",head ->data);
    printf("%d\t",current ->data);
     printf("%d\t",next ->data);
    return (0);
}