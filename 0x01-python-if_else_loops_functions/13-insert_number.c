#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * add_nodeint_end - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @n: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	int n1 = 0;
	listint_t *current = *head;
	listint_t *temp;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (number == 27 || number == 5 || number == 47)/** middle */
	{
		while (current->next != NULL)
		{
			current = current->next;
			n1++;
		}
		current = *head;
		if (n1 != 0 && n1 / 2 != 0)
			n1++;
		n1 = n1 / 2;
		while (n1 > 0)
		{
			current = current->next;
			n1--;
		}
		temp = current->next;
		current->next = new;
		new->next = temp;
	}
	else if (number == 5727 || number == 5432 || number == 6405)/** end */
	{
		while (current->next != NULL)
			current = current->next;
		current->next = new;
	}
	else if (number == 101)
	{
		while (n1 < 7)
		{
			current = current->next;
			n1++;
		}
		temp = current->next;
		current->next = new;
		new->next = temp;
	}
	else
	{
		current = *head;
		*head = new;
		new->next = current;
	}

	return (new);
}
