#include <iostream>
using namespace std;

int main()
{
    int myArray[] = {2, 4, 5, 6, 8};
   //size: 5
    int i;
    //Using a for loop to iterate through myArray and print out each element and its corresponding index
   for(i = 0; i < 5; i++)
   {
    cout << "The index of: " << myArray[i] << " is " << i << endl;  
   }
    return (0);
}