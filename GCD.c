#include <stdio.h>

#include <stdlib.h>
 //Function definition
void GCD();
void integerRepresentation();
void integerAddition();

int main() {
  // Fuction call to calculate GCD
  GCD();

  //Fuction call to represent decimals in base form
  integerRepresentation();
  //Fuction call to add integers
  integerAddition();

  return 0;
}
// fuction to find the GCD
void GCD() {
  int a, b, x, y, r;
  char start;
  // Produce gcd(a,b: positive integers)
  start:
    printf("Please Enter two values: ");
  scanf("%d %d", & a, & b);
  // if condition to accept only positive values
  if (a > 0 && b > 0) {

    x = a;
    y = b;
  } else {

    system("cls");
    goto start;
  }

  // Using while loop to calculate the gcd
  while (y != 0) {
    r = x % y;
    x = y;
    y = r;

  }
  printf("The GCD of %d and %d is: %d\n\n\n\n", a, b, x);
  //system ("cls");

}
//Function fpr integer representation
void integerRepresentation()

{
  int b, n, i, r, digit, p, count = 0;
  char a[100];
  printf("Enter the decimal number and Base: ");
  scanf("%d %d", & n, & b);

  p = n;
  do {
    r = p % b;
    digit = '0' + r;
    if (digit > '9')
      digit = digit + 7;
    a[count] = digit;
    count++;
    p = p / b;
  } while (p != 0);
  printf("Base %d equivalent of the number %d is: ", b, n);
  for (i = count - 1; i >= 0; --i)
    printf("%c", a[i]);
  printf("\n\n\n");

}
//function for integer addition

void integerAddition() {
  long a, b;
  int i = 0, r = 0, sum[20];

  printf("Enter two  binary numbers: ");
  scanf("%ld %1d", & a, & b);

  while (a != 0 || b != 0) {
    sum[i++] = (a % 10 + b % 10 + r) % 2;
    r = (a % 10 + b % 10 + r) / 2;
    a = a / 10;
    b = b / 10;
  }
  if (r != 0)
    sum[i++] = r;
  --i;
  printf("Sum of a and b binary numbers are: ");
  while (i >= 0)
    printf("%d", sum[i--]);
  return 0;
}
