//This is a prgram that takes inputs from a user and prints sum and average of the inputs
 #include <stdio.h>
 int main ()
 {
    //Declaring varuables
    int num[5];
    int i, sum =0;
    float average;
    float Deviation;

    printf("Enter five random values: \t");
    /**using for loop to take inputs from user and also formulate sum and deviation
     * **/
    for(i=0;i<5;i++){
        scanf("%d",&num[i]);
         sum = sum + num[i];
          Deviation = num[i]-average;
        }
    // calculating average of five inputs
    average = sum/5;
        //Printing out sum and average of the inputs
     printf("Sum of the values is: %d\n",sum);
     printf("The average of the values is: %.1f \n\n\n",average);
// using a for loop to print out the deviation from average
    for(i=0;i<5;i++){
        printf("Deviation of the value %d from mean is: %.1f\n",num[i],Deviation);
        }
    
    
    return 0;
 }
