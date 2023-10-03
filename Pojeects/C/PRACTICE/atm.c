#include <stdio.h>
#include <stdlib.h>

int main()
/*
Title:    My first ATM project.
Name: Isaac yaw Amponsah
Index No: 3023120
Programme: Computer Engineering 1
 */
{
    //Declaring my variables
    int pin;
    int amount = 5000;
    int balance, withdraw, deposit;
    char Choice;
    // Start command to send the user to the initial stage
    Start:
        //Requesting input from the user

    printf("Enter your pin: ");
    scanf("%d",&pin);
    //Pin initialization
    if(pin==2704){
            //Displaying Options for the user to make a choice.
        printf("WELCOME DEAR CUSTOMER \n\n");
        printf("1. Withdraw Money \n");
        printf("2. Deposit Money \n");
        printf("3. Check Balance \n");
        printf("4. Transfer Money \n");
        printf("5. Quit \n");
        printf("Enter Service Choice: ",Choice);
        scanf("%d",&Choice);

// using conditional statements to execute the users choice.
    }

    else{
        printf("Invalid PIN\n");
         goto Start;
    }

    switch(Choice){
        //Case 1 to initiate a withdrawal process.
        case 1 :
        printf("Please Enter an amount to withdraw: ");
        scanf("%d",&withdraw);
        if(withdraw>5000){
            printf("Your balance is insufficient.\n");

        }
        else if(withdraw<=50){
            printf("Sorry!, Minimum Withdrawal is above $50.\n");
        }
        else{
            balance = amount- withdraw;
            printf("Collect Cash. \n");
            printf("Current balance is : $%d. \n",balance);
            break;

        }
        // Case 2 for the user to make a deposit.
        case 2 :
            printf("Enter an amount to Deposit: ");
            scanf("%d", &deposit);
            balance = amount + deposit;
            printf("Your current Balance is : $%d\n", balance);
            break;
            // case 3 for the user to check their balance
        case 3 :
            printf("Your Available Balance is : $%d",amount);
            break;
            // case for the user to make a transfer.
        case 4:
            printf("Sorry this Service has been disabled Temporarily.\nContact the Bank for more Details.\n");
            break;
        case 5 :
            printf("Thanks for using our Service.");
            break;
        default:
            printf("Your choice is Invalid.\n");
            goto Start;

    }

    return 0;
}
