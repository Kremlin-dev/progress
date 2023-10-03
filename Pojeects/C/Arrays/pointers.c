#include <stdio.h>

/**
 *main - Pointers
 *Return: Always 0
*/

int main(void)
{
  int a;
  a = 6;
  int *p;
  p = &a;
  printf("%d\n", a);
  printf("%d\n", &a);
  printf("%d\n", &p);
  printf("%d\n", *p);
  printf("%d\n", p + 1);
  return (0);
}