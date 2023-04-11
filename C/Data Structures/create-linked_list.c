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
    struct node *next;
};
void print(struct node *m)
{
    while (m != NULL)
    {
        printf("%d\t", m ->data);
        m = m -> next;
    }
}
int main(void)
{   
    struct node *head = malloc(sizeof(struct node));
    struct node *current = malloc(sizeof(struct node));
    struct node *third = malloc(sizeof(struct node));

    head ->data = 789;
    head ->next = current;

    current -> data = 45;
    current ->next = third;

    third ->data = 900;
    third ->next = NULL;
    print(head);

    //printf("%d %d %d", head->data, current ->data, third ->data);


    return (0);
}