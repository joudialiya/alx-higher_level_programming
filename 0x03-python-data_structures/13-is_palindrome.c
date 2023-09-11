#include "lists.h"

/**
 * is_palindrome - checks if a linked list is palindrom
 * @head: ptr to wher the hed is
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = NULL;
	listint_t *end = NULL;

	end = NULL;
	current = *head;
	while (current != end)
	{
		listint_t *mirrored = NULL;

		mirrored = current;
		while (mirrored->next != end)
		{
				mirrored = mirrored->next;
		}
		if (current->n != mirrored->n)
				return (0);
		end = mirrored;
		current = current->next;
	}
	return (1);
}
