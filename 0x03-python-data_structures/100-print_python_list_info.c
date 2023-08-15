#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints some basic info about
 * Python lists.
 * @p: PyObject
 * Return: no value
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *alist;
	PyObject *element;
	long int size;
	long int idx;

	size = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", size);
	alist = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", alist->allocated);

	for (idx = 0; idx < size; idx++)
	{
		element = PyList_GetItem(p, idx);
		printf("Element %ld: %s\n", idx, Py_TYPE(element)->tp_name);
	}
}
