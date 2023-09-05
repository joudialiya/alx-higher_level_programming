#include "lists.h"

/**
 * insert_node - insert the nod to a sorted linked list
 * @head: head ptr addr
 * @number: value
 * Return: the node or NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL;
	listint_t *current = NULL;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	current = *head;
	if (*head == NULL || number < (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	/*
	 * searcing for the node that is just before
	 * the node that is grater than number
	 */
	while (current->next && number > current->next->n)
		current = current->next;
	new->next = current->next;
	current->next = new;
	return (new);
}
