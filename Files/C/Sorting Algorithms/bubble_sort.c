#include <stdio.h>
#include <string.h>
#include <stdlib.h>
/**
 * Bubble sort Algorithm is the simplest for of sorting Algorithms
 * It works by comparing adjacent values and swapping them.
 * 
 * bubble_sort - bubble sort function
 * @array: Array containg list of items to be sorted
 * @size: size of items contained in the array
 * Return: sorted items
*/
void print_swap(int *array, size_t size)
{
    int i;
    for (i = 0; i < size; i++)
    {
        printf("%d ", array[i], i + 1 == size ? "}" : ", ");
    }
}
void bubble_sort(int *array, size_t size)
{
    int i, j, temp = 0;

    for (i = 0; i < size; i++)
    {
        for (j = 0; j < size - i - 1; j++)
        {
            if (array[j] > array[ j + 1]) 
            {
                temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;
               print_swap(array, size);
               printf("\n");
            }
        }
    }

}

int main() {
    int arr[] = { 64, 34, 25};
    int n = sizeof(arr) / sizeof(arr[0]);
    bubble_sort(arr, n);
    printf("Sorted array: \n");
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    return 0;
}