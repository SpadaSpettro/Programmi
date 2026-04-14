#include <iostream>
#include <limits> //Necessaria per numeric_limits

using namespace std;

//Dichiarazione funzioni
int controllaInt();

int main () {
   char continua; //Variabili
   
   do {
      int n;
      cout << "\nQuesto programma chiede di inserire un numero intero compreso tra 1 e 100 (inclusi) e, a seconda del numero inserito, esegue diverse operazioni.\n" << endl;
      cout << "Inserire un numero intero compreso tra 1 e 100 (inclusi): ";
      n = controllaInt();
      while (n<1 || n>100) {
         cout << "Inserimento non valido, si prega di inserire un numero adeguato: ";
         n = controllaInt();
      }
      if (n==50) {
         cout << "541!" << endl;
      } else if (n%2!=0 && n<50) {
         cout << n << "x2=" << n*2 << endl;
      } else if (n%2!=0 && n>50) {
         cout << n << "x" << n << "=" << n*n << endl;
      } else {
         cout << n << "/2=" << n/2 << ", senza resto." << endl;
      }
      cout << "\nInserire 'y' per continuare a eseguire il programma, inserire qualsiasi altro valore per uscire: ";
      cin >> continua;
   }
   while (continua=='y');
   cout << "Grazie per aver utilizzato il programma";

   cin.ignore(numeric_limits<streamsize>::max(), '\n');
   cin.get();
   return 0;
}

//Definizione funzioni
int controllaInt() {
   float valore;
   while (!(cin >> valore) || valore!=static_cast<int>(valore)) {
      cout << "Errore. Valore non riconosciuto. Riprovare: ";
      cin.clear();
      cin.ignore(numeric_limits<streamsize>::max(), '\n');
   }
   cin.ignore(numeric_limits<streamsize>::max(), '\n');
   return static_cast<int>(valore);
}