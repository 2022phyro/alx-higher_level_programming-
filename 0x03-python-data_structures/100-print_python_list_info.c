#include <stdio.h>
#include <Python.h>
#include <object.h>
#include <listobject.h>
void print_python_list_info(PyObject *p)
{
	int i, j, mem;
	PyListObject *ab = (PyListObject *)(p);

	i = Py_SIZE(p);
	j = 0;
	mem = ab->allocated;

	printf("[*] Size of the Python List = %d\n", i);
	printf("[*] Allocated = %d\n", mem);
	for (j = 0; j < i; j++)
        {
		printf("Element %d: %s\n", j, ab->ob_item[j]->ob_type->tp_name);
	}

}
