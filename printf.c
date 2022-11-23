#include <stdio.h>
#include <string.h>
#include <stdarg.h>

int _printf(const char *format, ...)
{
    va_list arg;
    va_start(arg, format);
    int i = 0;

    while (format && format[i])
    {
        if(format[i] == '%')
        {
            i++;
            switch (format[i])
            {
            case 'c':
            {
                int x = va_arg(arg, int);
             printf("%c",x);
                break;
            }
            case 's':
            {
                char *x = va_arg(arg, char *);
                break;
                printf("%s",x);
            }

            }
        }
    }
}

int main(void)
{

    _printf("%d",5);  
}