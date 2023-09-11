#include "lists.h"
/**
 * length_list - the lenght of a linked list
 * @head: head of the list
 * Return: the length
 */
int length_list(listint_t *head)
{
	if (head == NULL)
		return (0);
	return (1 + length_list(head->next));
}

/**
 * is_palindrome - checks if a linked list is palindrom
 * @head: ptr to wher the hed is
 * Return: 0 or 1
 */
int is_palindrome(listint_t **head)
{
	int index = 0;
	int length = 0;
	listint_t *current = NULL;

	length = length_list(*head);
	current = *head;
	while (index < length / 2)
	{
		listint_t *mirrored = current;
		int mirrored_index = length - 1 - index;
		int i = index;

		while (i < mirrored_index)
		{
			mirrored = mirrored->next;
			++i;
		}
		if (current->n != mirrored->n)
			return (0);
		++index;
		current = current->next;
	}
	return (1);
}
