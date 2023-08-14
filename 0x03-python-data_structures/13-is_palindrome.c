#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * An empty list is considered a palindrome
 * @head: beginning of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *begin;
	int *copy, a = 0, length = 0;

	begin = *head;
	while (begin != NULL)
	{
		length++;
		begin = begin->next;
	}
	copy = malloc(sizeof(int) * (length));
	if (copy == NULL)
	{
		return (0);
	}

	a = 0;
	begin = *head;
	while (begin != NULL)
	{
		copy[a++] = begin->n;
		begin = begin->next;
	}

	a = 0;
	length--;
	while (copy[a] == copy[length])
	{
		if (a == length || a > length)
		{
			free(copy);
			return (1);
		}
		a++;
		length--;
	}

	free(copy);
	return (0);
}
