#include <Python.h>

static PyObject* multiplier(PyObject* self, PyObject* args) {
	long a, b;

	if (!PyArg_ParseTuple(args, "ll", &a, &b)) {
		return NULL;
	}

	return PyLong_FromLong(a * b);
}

static PyMethodDef Methods[] = {
	{ "multiplier", multiplier, METH_VARARGS, "Multiply two longs" },
	{ NULL, NULL, 0, NULL }
};

static struct PyModuleDef c_extension_module = {
	PyModuleDef_HEAD_INIT,
	"c_extension",
	"Example C extension",
	-1,
	Methods
};

PyMODINIT_FUNC PyInit_c_extension(void) {
	return PyModule_Create(&c_extension_module);
}

