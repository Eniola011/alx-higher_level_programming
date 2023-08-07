#include "lists.h"

/**
 * check_cycle - a function in C that checks if a singly
 * linked list has a cycle in it.
 * @list: pointer to linkedlist
 * Return: 0 if there is no cycle, 1 if there is a cycle
 *
 */
int check_cycle(listint_t *list)
{
	listint_t *previous;
	listint_t *nextnode;

	previous = nextnode = list;

	while (list && previous && nextnode && previous->next && nextnode->next)
	{
		previous = previous->next;
		nextnode = nextnode->next->next;

		if (!nextnode || !previous)
		{
			return (0);
		}
		if (nextnode->next == previous)
		{
			return (1);
		}
	}

	return (0);
}
