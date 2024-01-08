#include <Python.h>
#include <stdio.h>

void print_python_list_info(po *p) {
    plo *list = (plo *)p;
    Py_ssize_t size, allocated, i;
    po *item;

    size = PyList_Size(p);
    allocated = list->allocated;

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", allocated);

    for (i = 0; i < size; i++) {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

