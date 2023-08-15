#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * An empty list is considered a palindrome
 * @head: beginning of list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *begin = *head;
	int *copy = NULL, a = 0, length = 0;

	if (*head == NULL || head == NULL || (*head)->next == NULL)
	{
		return (1);
	}
	while (begin)
	{
		length++;
		begin = begin->next;
	}

	copy = malloc(sizeof(int) * length);
	begin = *head;
	while (begin)
	{
		copy[a++] = begin->n;
		begin = begin->next;
	}

	for (a = 0; a < length / 2; a++)
	{
		if (copy[a] != copy[length - 1 - a])
		{
			free(copy);
			return (0);
		}
	}

	free(copy);
	return (1);
}
