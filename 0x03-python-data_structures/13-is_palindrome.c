#include "lists.h"

/**
 * is_palindrome - checks if a linked list is palindrom
 * @head: ptr to wher the hed is
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = NULL;
	int list[2048];
	int size = 0;
	int index = 0;

	current = *head;
	while (current)
	{
		list[size] = current->n;
		++size;
		current = current->next;
	}
	
	while (index != size / 2)
	{
		int mirrored_index = size - 1 - index;

		if (list[index] != list[mirrored_index])
				return (0);
		++index;
	}
	return (1);
}
