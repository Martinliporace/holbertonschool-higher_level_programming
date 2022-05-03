#include "lists.h"

/**
* check_cycle -  checks if a singly linked list has a cycle in it.
* @list: list
*
* Return: 0 if there is no cycle, 1 if there is a cycle
*/


int check_cycle(listint_t *list)
{
int salida = 0;

listint_t *one = list, *two = list;
	if (list == NULL)
		return (0);
	while (one != NULL && two != NULL && two->next != NULL)
		{
		one = one->next;
		two = two->next->next;
		if (one == two)
			{salida = 1;
			return (salida);
}
}
return (salida);
}
