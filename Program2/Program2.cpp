#define NOMINMAX
#include <iostream>
#include <cmath>
#include <limits> // Necessary for "numeric_limits"
#include <string>
#include <format>
#ifdef _WIN32
#include <Windows.h> // Used to change terminal encoding
#endif
using namespace std;

// Functions declaration
double input_check();

int main()
{
#ifdef _WIN32
   // Forces terminal to use UTF-8 encoding
   SetConsoleOutputCP(CP_UTF8);
   SetConsoleCP(CP_UTF8);
#endif
   double sum = 0, min = 0, max = 0; // Variables

   cout << "\nThis program calculates the sum and arithmetic mean of the entered numbers, plus a special calculation!\n\nHow many numbers do you want to enter?\n";
   int numbers = input_check();
   cout << format("Enter {} numbers:\n", numbers);

   // Input acquisition loop
   for (auto i = 0; i < numbers; i++)
   {
      cout << format("Number {}:\t", i + 1);
      double n = input_check();
      sum += n;
      if (n < min || i == 0)
      {
         min = n;
      }
      if (n > max || i == 0)
      {
         max = n;
      }
   }

   cout << format("\nLowest number: {}; Highest number: {}\nThe sum of the {} entered numbers is: {}", min, max, numbers, sum) << endl;
   double avg = sum / numbers;

   cout << format("The arithmetic mean of the {} entered numbers is: {:.10g}\n", numbers, avg);
   if (avg > 100 && fmod(sum, 2.0) == 0.0)
   {
      cout << format("The square of the arithmetic mean is: {:.10g}\n", avg * avg);
   }
   else
   {
      cout << format("The triple of the sum is: {:.10g}\n", sum * 3.0);
   }

   cin.ignore(numeric_limits<streamsize>::max(), '\n');
   cout << "\nPress ENTER to close the program...";
   cin.get();
   return 0;
}

// Functions definition
double input_check()
{
   string line = "";
   double input = 0.0;
   while (true)
   {
      if (!getline(cin, line) || line.empty()) // 1. Reads the entire string to ensure there is no "waste" left in the buffer
      {
         continue;
      }
      try
      {
         size_t numbers = 0;
         // 2. "stod" converts string into double
         // Saves into "numbers" the number of characters read as numbers
         input = stod(line, &numbers);

         // 3. Checks if the conversion stopped before the end of the line (e.g. user typed "15.5abc", therefore the characters read as numbers are less than the total lenght of the line)
         // If they are equal, the input is perfectly valid.
         if (numbers == line.size())
         {
            return input;
         }
         else
         {
            cout << "Error. Invalid input. Input only numbers: ";
         }
      }

      // 4. Exceptions management: if "stod" fails completely (e.g. the user types "hello"), throw an exception "invalid_argument" which is caught to avoid the crash of the program
      catch (const std::invalid_argument &)
      {
         cout << "Error. Non-numeric input. Try again: ";
      }
      // Catch the error when the entered number is too big to be managed
      catch (const std::out_of_range &)
      {
         cout << "Error. Number too big. Try again: ";
      }
   }
}