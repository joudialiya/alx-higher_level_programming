#include "Python.h"
#include "listobject.h"
#include "string.h"
void print_python_bytes(PyObject *p)
{
		long int i = 0;
		Py_ssize_t size = ((PyVarObject *)p)->ob_size;

		printf("[.] bytes object info\n");
		if (!PyBytes_Check(p))
		{
			printf("  [ERROR] Invalid Bytes Object\n");
			return;
		}
		PyBytesObject *ob = (PyBytesObject *)p;
		printf("  size: %ld\n", size);
		printf("  trying string: %s\n", ob->ob_sval);
		printf("  first %ld bytes: ", (size + 1) < 10 ? size + 1 : 10);
		for (i = 0; i < size + 1 && i < 10; ++i)
		{
			printf("%02x", ob->ob_sval[i] & 0xff);
			if (i < size || i < 9)
					printf(" ");
		}
		printf("\n");
}
void print_python_list(PyObject *p)
{
		Py_ssize_t size = ((PyVarObject *)p)->ob_size;
		PyListObject *list = (PyListObject *)p;
		Py_ssize_t index = 0;

		printf("[*] Python list info\n");
		printf("[*] Size of the Python List = %ld\n", size);
		printf("[*] Allocated = %ld\n", list->allocated);
		while(index < size)
		{
				PyObject *item = list->ob_item[index];
				

				printf("Element %ld: %s\n", index, (((PyObject*)(item))->ob_type)->tp_name);
				if (strcmp((((PyObject*)(item))->ob_type)->tp_name, "bytes") == 0)
						print_python_bytes(item);
				++index;
		}
}
