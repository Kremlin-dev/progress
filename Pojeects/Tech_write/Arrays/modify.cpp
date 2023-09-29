#include <iostream>
using namespace std;

int main()
{
    int myArray[] = {2, 4, 5, 6, 8};
   //size: 5
   cout << "Before modification: " << myArray[0] << endl;  //printing out first element in the array
   myArray[0] = 80; // Reinitialize first element in the array to 80
   cout <<"After modification: " << myArray[0] << endl; //printing out first element in the array

    return (0);
}