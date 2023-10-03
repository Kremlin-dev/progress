#include <stdio.h>
#include <stdarg.h>

/**
 * add - adds variable number of arguements
 * @n: last fixed argument
 * Return: int value
*/
int add(int n, ...)
{
    va_list arg;
    va_start(arg, n);
    int sum = 0;

    for (int i = 0; i < n; i++)
        {
             sum = sum + va_arg(arg, int);
        }
        return sum;
    va_end(arg);
   
}
/**
 * main - calls an add function and prints the sum
 * 
 * Return: Always 0
*/
int main(void)
{
    int sum = add(4, 45,0,2,5);
    printf("%d", sum);

}