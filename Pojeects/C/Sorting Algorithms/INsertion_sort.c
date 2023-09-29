#include <stdio.h>
/**
 * INsertion sort works on the basis of inserting each element at its rightful place after each pass
 * The first element is considered as sorted and the rest are compared to it
 * Any element greater than the first element is placed on the right side of it
 * Any elemnt lesser than  the first element is plaaced on the left hand side
 * Two loops are used to implement this sorting algorithm. 
 * 
 */

void INsertion_sort(int arr[], int n)
{
    int i, j, key;

    for (i = 1; i < n; i++)
    {
        key = arr[i];
        j = i -1;

        while (j >= 0 && arr[j] > key)
        {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j+1] = key;
    }
}

int main(void)
{
    int i;
    int arr[] = {3, 7,1,9,23,5,0,12};

    int size = sizeof(arr) / sizeof(int);
    INsertion_sort(arr, size);

    for ( i = 0; i < size; i++)
    {
        printf("%d\n", arr[i]);
    }

    return (0);
}