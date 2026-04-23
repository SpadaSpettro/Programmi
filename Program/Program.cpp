#define NOMINMAX // Deactivates min e max Windows macros
#include <iostream>
#include <limits> // Necessary for "numeric_limits"
#include <string>
#include <charconv> // Necessary for "from_chars"
#include <format>
#ifdef _WIN32
#include <Windows.h> // Used to change terminal's encoding
#endif
using namespace std;

// Program constants definition
constexpr int MIN_VAL = 1;
constexpr int MAX_VAL = 100;
constexpr int THRESHOLD = 50;

// Functions declaration
int inputInt_check();

int main()
{
#ifdef _WIN32
   // Forces terminal to use UTF-8 encoding
   SetConsoleOutputCP(CP_UTF8);
   SetConsoleCP(CP_UTF8);
#endif

   // Variables
   char continuation = 'n';
   int numbers = 0, fifty = 0, twoTimes = 0, square = 0, half = 0;

   cout << format("\nThis program asks the user to enter an integer number between {} and {} (included); based on the entered number, the program will perform a different operation.\n", MIN_VAL, MAX_VAL);
   do
   {
      int n = 0;
      cout << format("\nEnter an integer number between {} e {} (included): ", MIN_VAL, MAX_VAL);
      n = inputInt_check();
      numbers++;
      while (n < MIN_VAL || n > MAX_VAL)
      {
         cout << "Invalid input, please enter a valid number: ";
         n = inputInt_check();
         numbers++;
      }

      // The program performs different operations based on the condition
      if (n == THRESHOLD)
      {
         cout << "541!" << endl;
         fifty++;
      }
      else if (n % 2 != 0)
      {
         if (n < THRESHOLD)
         {
            cout << format("{}x2 = {}", n, n * 2) << endl;
            twoTimes++;
         }
         else
         {
            cout << format("{}² = {}", n, n * n) << endl;
            square++;
         }
      }
      else
      {
         cout << format("{}/2 = {}, no remainder.", n, n / 2) << endl;
         half++;
      }

      // Safe continuation request
      cout << "\nType \"y\" to keep running the program, type anything else to exit it: ";
      string answer;
      getline(cin, answer);
      if (!answer.empty())
      {
         continuation = answer[0]; // Gets only the first typed character
      }
      else
      {
         continuation = 'n'; // Exits when only ENTER is pressed
      }
   } while (continuation == 'y' || continuation == 'Y');

   cout << format("\nTotal numbers entered by the user: {}\nCases in which a number was 50: {}\nCases in which a number was doubled: {}\nCases in which a number was squared: {}\nCases in which a number was halved: {}\n\nThank you for using the program.", numbers, fifty, twoTimes, square, half);
   cin.ignore(numeric_limits<streamsize>::max(), '\n');
   cout << "Press ENTER to exit the program...";
   cin.get();
   return 0;
}

// Functions definiton
int inputInt_check()
{
   float input;
   while (!(cin >> input) || input != static_cast<int>(input))
   {
      cout << "Error. Unrecognized input. Try again: ";
      cin.clear();
      cin.ignore(numeric_limits<streamsize>::max(), '\n');
   }
   cin.ignore(numeric_limits<streamsize>::max(), '\n');
   return static_cast<int>(input);
}