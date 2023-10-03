#include <stdio.h>
#include <stdlib.h>

/**
 * main - Calls a function Be_ginning to insert a node in a linked list
 * 
 * Return: Always 0
*/

struct node
{
    int data;
    struct node *next;
};

struct node* add_beginning(struct node *m, int n);

int main(void)
{
    struct node *head = malloc(sizeof(struct node));
    struct node *primiere_node = malloc(sizeof(struct node));

    head -> data = 87;
    head -> next = primiere_node;
    int data = 700;
    head = add_beginning(head, data);
    primiere_node = head;
    
    while (primiere_node != NULL)
    {
        printf("%d", primiere_node -> data);
        primiere_node= primiere_node->next;
    }
    
    return (0);
}
struct node* add_beginning(struct node *head, int n)
{
    struct node *primiere_node = malloc(sizeof(struct node));
    head -> next = primiere_node;
    head = primiere_node;
    return head;
}