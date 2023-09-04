#include "lists.h"

/**
 * check_cycle - using floyd algorithm
 * @list: the linked list
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
