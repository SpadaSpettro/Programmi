#define NOMINMAX
#include <iostream>
#include <cmath>
#include <Windows.h> //Necessaria per cambiare la codifica del terminale
#include <limits> //Necessaria per numeric_limits

using namespace std;

//Dichiarazione funzioni
double controllaDouble();

int main() {
   // Forza il terminale a usare la codifica UTF-8
   SetConsoleOutputCP(CP_UTF8);
   SetConsoleCP(CP_UTF8);

   double n, somma=0, media=0; //Variabili
   
   cout << "Questo programma calcola la somma e la media aritmetica di 10 numeri, più un calcolo speciale!\n" << endl;
   cout << "Inserire 10 numeri:" << endl;
   for (int i=0; i<10; i++) {
      cout << i+1 << "° numero:\t";
      n = controllaDouble();
      somma+=n;
   }
   cout << "\nLa somma dei 10 numeri inseriti è: " << somma << "."<<endl;
   media=somma/10.0;
   cout << "La media aritmetica dei 10 numeri inseriti è: " << media << "." << endl;
   if (media>100 && fmod(somma, 2)==0) {
      cout << "Il quadrato della media è: " << media*media << "." << endl;
   } else {
      cout << "Il triplo della somma è: " << somma*3.0 << "." << endl;
   }

   cin.ignore(numeric_limits<streamsize>::max(), '\n');
   cin.get();
   return 0;
}

//Definizione funzioni
double controllaDouble() {
   double valore;
   while (!(cin >> valore)) {
      cout << "Errore. Valore non riconosciuto. Riprovare: ";
      cin.clear();
      cin.ignore(numeric_limits<streamsize>::max(), '\n');
   }
   cin.ignore(numeric_limits<streamsize>::max(), '\n');
   return valore;
}