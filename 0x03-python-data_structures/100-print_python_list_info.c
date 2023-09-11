#include "Python.h"
#include "listobject.h"

void print_python_list_info(PyObject *p)
{
		Py_ssize_t size = PyList_Size(p);
		Py_ssize_t allocated = ((PyListObject *)p)->allocated;
		Py_ssize_t index = 0;

		printf("[*] Size of the Python List = %ld\n", size);
		printf("[*] Allocated = %ld\n", allocated);
		while(index < size)
		{
				PyObject *item = PyList_GetItem(p, index);

				printf("Element %ld: %s\n", index, Py_TYPE(item)->tp_name);
				++index;
		}
}
