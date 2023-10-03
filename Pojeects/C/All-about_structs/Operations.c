#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * struct op - Struct op
 *
 * @op: The operator
 * @f: The function associated
 */

struct opt
{
    char *op;
    int (*f)(int a, int b);
};
struct opt operation;

int op_add(int a, int b)
{
    return (a + b);
}
///////////////////////////////////
int op_sub(int a, int b)
{
    return (a - b);
}
////////////////////////////////////
int op_mul(int a, int b)
{
    return (a * b);
}
/////////////////////////////////////
int op_div(int a, int b)
{
    return (a / b);
}
/////////////////////////////////////
int op_mod(int a, int b)
{
    return (a % b);
}
//////////////////////////////////////

int (*get_op_func(char *s))(int, int)
{
    struct opt ops[] =
    {
        {"+", op_add},
        {"-", op_sub},
        {"*", op_mul},
        {"/", op_div},
        {"%", op_mod},
        {NULL, NULL},
    };
    int i =0;

    while (i < 5)
    {
        if (*(ops[i]).op == *s)
        {
            return (ops[i].f);
        }
    }
}

int main(int argc, char *argv[])
{
	int a, b;
	int (*operation)(int, int);

	if (argc != 4)
	{
		printf("Error\n");
		exit(98);
	}

	if (argv[2][1])
	{
		printf("Error\n");
		exit(99);
	}

	operation = get_op_func(argv[2]);

	if (operation == NULL)
	{
		printf("Error\n");
		exit(99);
	}

	a = atoi(argv[1]);
	b = atoi(argv[3]);

	printf("%d\n", operation(a, b));
	return (0);
}