#include "lists.h"

/**
 * is_palindrome - checks if a linked list is palindrom
 * @head: ptr to wher the hed is
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = NULL;
	listint_t **list = NULL;
	int size = 0;
	int index = 0;

	current = *head;
	while (current)
	{
		list = realloc(list, sizeof(listint_t *) * (size + 1));
		list[size] = current;
		++size;
		current = current->next;
	}
	
	while (index != size / 2)
	{
		int mirrored_index = size - 1 - index;

		if (list[index]->n != list[mirrored_index]->n)
				return (0);
		++index;
	}
	return (1);
}
