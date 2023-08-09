#include "lists.h"

/**
 * insert_node - a function in C that inserts a number into a
 * sorted singly linked list.
 * @head: beginning of a list
 * @number: int
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *head1, *head0, *newnode;

	head1 = *head;
	newnode = malloc(sizeof(listint_t));

	if (newnode == NULL)
	{
		return (NULL);
	}
	while (head1 != NULL)
	{
		if (head1->n > number)
		{
			break;
		}
		head0 = head1;
		head1 = head1->next;
	}

	newnode->n = number;

	if (*head == NULL)
	{
		newnode->next = NULL;
		*head = newnode;
	}
	else
	{
		newnode->next = head1;
		if (head1 == *head)
		{
			*head = newnode;
		}
		else
		{
			head0->next = newnode;
		}
	}

	return (newnode);
}
