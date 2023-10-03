#include <stdio.h>
#include <stdlib.h>
#include <time.h>


/*
PROJECT NAME: BUILDING A CAR RENTAL SYSTEM.
GEOUP 11
NB: Member names are beneath source code.


DEFAULT PASSWORD AND USERNAME THAT ALLOWS THE USER TO LOGIN.

USERNAME: GROUP11
PASSWORD: RENTALSYSTEM

NEW USERS CAN CHOOSE TO REGISTER AND LOGIN WITH THIER OWN DETAILS

**/
//Function declaration.
void display ();
void login ();
void Registration ();
void Payment ();
void delay ();
//Declaration of Global Variables.
char R_Password[20];		//Registration Password of the new user
char confirm_password[20];	// Variable to confirm the password entered by the new user.
char R_Username[20];		// Registration Username of the new user.
char Username[20];		// Username container
char name[20];			// Stores the real name of the user
char Password[10];		// Stores the Password of both old and new users
int option;
int book, model;
char MainMenu;			// label
char begin;			// label
int PriceperDay, NumberofDays, TotalFee;	// Containers to store price of rent per day,numberofdays and totalfee.


int
main ()
{


start:
  printf ("HELLO!, WELCOME TO GROUP 11's CAR RENTAL SYSTEM.\n\n");

// Asking the user to login or Register a new account into the system.
  printf ("Enter 0 to Login or 1 to register: ");
  scanf ("%d", &option);
  if (option == 0)
    {
      // Function call Login, if the user chooses to Login.
      system ("cls");
      login ();
    }
  else if (option == 1)
    {
      system ("cls");
      //function call to Register a new Account.
      Registration ();
    }

  else
    {

      printf ("Incorrect input.\n");
      for (int i = 0; i < 1; i++)
	{


	  delay (1);
	  system ("cls");
	}



      goto start;
    }





  return 0;
}

// Login Function Definition.
void
login ()
{

  printf ("WELCOME TO THE LOGIN PAGE.\n\n\n");
begin:
  // Asking user to Enter login Username and Password.
  printf ("Please Enter your username: ");
  scanf ("%s", Username);

  printf ("Please Enter your password: ");
  scanf ("%s", Password);


  // using if condition to compare Username and Registration Username
  if (strcmp (Username, R_Username) == 0
      && strcmp (Password, R_Password) == 0)
    {
      system ("CLS");
    start:
      //Calling Display function to Display list of Cars available.
      display ();

      printf ("Enter a Number on the List: ");
      scanf ("%d", &model);


//Printing out user's Option using Switch case.
      switch (model)
	{
	case 1:
	  printf ("  SUZUKI | Celerio\n");
	  printf
	    ("Press 1 to book this Vehicle or 0 to return to Main menu: ");
	  scanf ("%d", &book);
	  if (book == 1)
	    {
	      printf ("Enter the Number of Days of Renting: ");
	      scanf ("%d", &NumberofDays);
	      PriceperDay = 300;
	      TotalFee = PriceperDay * NumberofDays;
	      printf
		("You are to make payment of %d.00 GHc to the Cashier.\n",
		 TotalFee);
	      printf ("Enjoy your Ride!!!\n");
	    }
	  else if (book == 0)
	    {
	      system ("CLS");

	      goto start;
	    }

	  break;
	case 2:
	  printf ("  SUZUKI | Celerio\n");
	  printf
	    ("Press 1 to book this Vehicle or 0 to return to Main menu: ");
	  scanf ("%d", &book);
	  if (book == 1)
	    {
	      printf
		("Enter the Number of Days of Renting and any number to return to Main menu: ");
	      scanf ("%d", &NumberofDays);
	      PriceperDay = 300;
	      TotalFee = PriceperDay * NumberofDays;
	      printf
		("You are to make payment of %d.00 GHc to the Cashier.\n",
		 TotalFee);
	      printf ("Enjoy your Ride!!!\n");
	    }
	  else if (book == 0)
	    {
	      //This system clear allows the screen to be cleared before other displays.
	      system ("CLS");
	      goto start;
	    }
	  break;
	case 3:
	  printf ("   HONDA | Civic \n");
	  printf
	    ("Press 1 to book this Vehicle or 0 to return to Main menu: ");
	  scanf ("%d", &book);
	  if (book == 1)
	    {
	      printf
		("Enter the Number of Days of Renting and any number to return to Main menu: ");
	      scanf ("%d", &NumberofDays);
	      PriceperDay = 100;
	      TotalFee = PriceperDay * NumberofDays;
	      printf
		("You are to make payment of %d.00 GHc to the Cashier.\n",
		 TotalFee);
	      printf ("Enjoy your Ride!!!\n");
	    }
	  else if (book == 0)
	    {
	      system ("CLS");
	      goto start;
	    }
	  break;

	case 4:
	  printf ("    TOYOTA | Avalon \n");
	  printf
	    ("Press 1 to book this Vehicle or 0 to return to Main menu: ");
	  scanf ("%d", &book);
	  if (book == 1)
	    {
	      printf ("Enter the Number of Days of Renting: ");
	      scanf ("%d", &NumberofDays);
	      PriceperDay = 430;
	      TotalFee = PriceperDay * NumberofDays;
	      printf
		("You are to make payment of %d.00 GHc to the Cashier.\n",
		 TotalFee);
	      printf ("Enjoy your Ride!!!\n");
	    }
	  else if (book == 0)
	    {
	      system ("CLS");
	      goto start;
	    }
	  break;
	case 5:
	  printf ("    FORD | Explorer \n");
	  printf
	    ("Press 1 to book this Vehicle or 0 to return to Main menu: ");
	  scanf ("%d", &book);
	  if (book == 1)
	    {
	      printf ("Enter the Number of Days of Renting: ");
	      scanf ("%d", &NumberofDays);
	      PriceperDay = 250;
	      TotalFee = PriceperDay * NumberofDays;
	      printf
		("You are to make payment of %d.00 GHc to the Cashier.\n",
		 TotalFee);
	      printf ("Enjoy your Ride!!!\n");
	    }
	  else if (book == 0)
	    {
	      system ("CLS");
	      goto start;
	    }
	  break;
	case 6:
	  printf ("    TATA | Safari \n");
	  printf
	    ("Press 1 to book this Vehicle or 0 to return to Main menu: ");
	  scanf ("%d", &book);
	  if (book == 1)
	    {
	      printf ("Enter the Number of Days of Renting: ");
	      scanf ("%d", &NumberofDays);
	      PriceperDay = 250;
	      TotalFee = PriceperDay * NumberofDays;
	      printf
		("You are to make payment of %d.00 GHc to the Cashier.\n",
		 TotalFee);
	      printf ("Enjoy your Ride!!!\n");
	    }
	  else if (book == 0)
	    {
	      system ("CLS");
	      goto start;
	    }
	  break;
	case 7:
	  printf ("   MERCEDES | E-Class \n");
	  printf
	    ("Press 1 to book this Vehicle or 0 to return to Main menu: ");
	  scanf ("%d", &book);
	  if (book == 1)
	    {
	      printf ("Enter the Number of Days of Renting: ");
	      scanf ("%d", &NumberofDays);
	      PriceperDay = 500;
	      TotalFee = PriceperDay * NumberofDays;
	      printf
		("You are to make payment of %d.00 GHc to the Cashier.\n",
		 TotalFee);
	      printf ("Enjoy your Ride!!!\n");
	    }
	  else if (book == 0)
	    {
	      system ("CLS");
	      goto start;
	    }
	  break;
	case 8:
	  printf ("    Audi | Q3 \n");
	  printf
	    ("Press 1 to book this Vehicle or 0 to return to Main menu: ");
	  scanf ("%d", &book);
	  if (book == 1)
	    {
	      printf ("Enter the Number of Days of Renting: ");
	      scanf ("%d", &NumberofDays);
	      PriceperDay = 340;
	      TotalFee = PriceperDay * NumberofDays;
	      printf
		("You are to make payment of %d.00 GHc to the Cashier.\n",
		 TotalFee);
	      printf ("Enjoy your Ride!!!\n");
	    }
	  else if (book == 0)
	    {
	      system ("CLS");
	      goto start;
	    }
	  break;
	case 9:
	  printf ("    TOYOTA | Avalon \n");
	  printf
	    ("Press 1 to book this Vehicle or 0 to return to Main menu: ");
	  scanf ("%d", &book);
	  if (book == 1)
	    {
	      printf ("Enter the Number of Days of Renting: ");
	      scanf ("%d", &NumberofDays);
	      PriceperDay = 300;
	      TotalFee = PriceperDay * NumberofDays;
	      printf
		("You are to make payment of %d.00 GHc to the Cashier.\n",
		 TotalFee);
	      printf ("Enjoy your Ride!!!\n");
	    }
	  else if (book == 0)
	    {
	      system ("CLS");
	      goto start;
	    }
	  break;
	default:
	  printf ("Incorrect Input\n");
	  for (int i = 0; i < 1; i++)
	    {


	      delay (1);
	      system ("cls");
	    }


	  goto start;




	}

/** Comparing Username and password to default Username and Password set by the programmer
using the strcmp function.
**/
    }
  else if (strcmp (Username, "GROUP11") == 0
	   && strcmp (Password, "RENTALSYSTEM") == 0)
    goto start;
  else
    {
        system("cls");
      printf ("You have Entered either a wrong Password or Username.\n");
      goto begin;



    }
}

//Defining the Registration Function.
void
Registration ()
{

start:
  printf ("\n\nWELCOME TO THE REGISTRATION PAGE.\n\n");
  printf ("Enter your First Name: ");
  scanf ("%s", name);
  printf ("Enter your surname: ");
  scanf ("%s", name);
  printf ("Enter a Password: ");
  scanf ("%s", R_Password);
  printf ("Please Confirm your Password: ");
  scanf ("%s", confirm_password);
  if (strcmp (R_Password, confirm_password) == 0)
    {
// Allows user to login with new username and password they used to register.
      printf ("Enter your Username: ");
      scanf ("%s", R_Username);
      system ("CLS");



      login ();

    }

  else
    {
        system("cls");
      printf ("Your passwords  do not match.\n");
      goto start;
    }





}

// Defining the display function.
void
display ()
{

MainMenu:
  system ("cls");
  printf ("     THESE ARE THE LIST OF CARS AVAILABLE. \n");
  printf ("    CAR BRAND      MODEL       RENT PER DAY(GHC)  \n");
  printf ("------------------------------------------------- \n");
  printf ("1.     HYUNDAI    | Veloster |      250         | \n");
  printf ("2.    SUZUKI      | Celerio  |      300         | \n");
  printf ("3.      HONDA     |  Civic   |      100         | \n");
  printf ("4.     TOYOTA     |  Avalon  |      430         | \n");
  printf ("5.      FORD      | Explorer |      250         | \n");
  printf ("6.      TATA      |  Safari  |      250         | \n");
  printf ("7.    MERCEDES    |  E-Class |      500         | \n");
  printf ("8.      AUDI      |  Q3      |      340         | \n");
  printf ("9.     ISUZU      |  D-MAX   |      300         | \n");
  printf ("------------------------------------------------ \n");


}

void
delay (int number_of_seconds)
{
  // Converting time into milli_seconds
  int milli_seconds = 1000 * number_of_seconds;

  // Storing start time
  clock_t start_time = clock ();

  // looping till required time is not achieved
  while (clock () < start_time + milli_seconds);
}


/*
GROUP MEMBERS:
NAME                        INDEX NO.
1. Anim Ignatus              3023520
2. Amponsah yaw Isaac        3023120
3. Aniagyei Caleb Nana yaw   3023420
4. Andoh Joshua              3023320
5. Anaba Prince              3023220

*/
