class Calcolatrice:
	def __init__(self):
		self.cronologia: list[str] = []  # Type hint: specifichiamo che "cronologia" è una lista di stringhe.

	def defTipo(self, numero: float) -> int | float:
		if numero.is_integer():
			return int(numero)
		return numero

	def gestisciComando(self, comando: str) -> bool:
		match comando.strip().lower():  # Trasformiamo l'input in minuscolo e togliamo gli spazi ai lati per sicurezza.
			case "help":
				print("\n<<Per visualizzare la cronologia scrivi \"cronos\", per cancellarla scrivi \"c_cronos\"; digita \"x\" per uscire.>>\n")
				return True
			case "cronos":
				if self.cronologia:
					print(f"\n{'*'*34}\nCronologia:")
					for i in self.cronologia:
						print(i)
					print(f"{'*'*34}\n")
				else:
					print("Nessuna cronologia.\n")
				return True
			case "c_cronos":
				if self.cronologia:
					self.cronologia.clear()
					print("Cronologia cancellata.\n")
				else:
					print("Nessuna cronologia da cancellare.\n")
				return True
			case "x" | "X":
				print("\nChiusura dalla calcolatrice...\n")
				exit()  # Chiude il programma in modo pulito.
			case _:
				# Se non è nessuno dei comandi sopra elencati, restituisce "False".
				return False

	# Metodo per validare l'input numerico
	def richiedi_numero(self, testo_input: str) -> int | float:
		while True:
			valore = input(testo_input).strip()
			if self.gestisciComando(valore):
				continue  # Se è stato gestito un comando, ripete la richiesta del numero senza procedere alla conversione.
			try:
				numero = float(valore)  #Prova a convertire in float.
				return self.defTipo(numero)
			except ValueError:
				print("Errore: inserimento non valido. Devi inserire esclusivamente un numero o un comando.\n")

	# Metodo per validare l'input delle operazioni
	def richiedi_operazione(self, testo_input: str) -> str:
		operazioni_valide = ["+", "-", "*", "/"]
		while True:
			operazione = input(testo_input).strip()
			if self.gestisciComando(operazione):
				continue
			if operazione in operazioni_valide:
				return operazione
			else:
				print("Errore: inserimento non valido. Inserisci solo [+, -, * (moltiplicazione), / (divisione)] o un comando.\n")

	def esegui(self):
		TESTO1, TESTO_OPERAZIONE, TESTO2="Inserisci un numero:\n", "Scegli un'operazione [+, -, * (moltiplicazione), / (divisione)]:\n", "Inserisci un altro numero:\n"
		print("\nCALCOLATRICE - (digita 'help' per visualizzare i comandi, 'x' per uscire)\n\n0")
		
		while True:
			valore1_tot = self.richiedi_numero(TESTO1)
			operazione = self.richiedi_operazione(TESTO_OPERAZIONE)
			while True:
				valore2 = self.richiedi_numero(TESTO2)
				if operazione == "/" and valore2 == 0:
					print("Non puoi dividere per 0!\n")
				else:
					break  # Esce dal controllo divisione e procede al calcolo.
			calcolo = f"{valore1_tot} {operazione} {valore2} ="
			match operazione:
				case "+": valore1_tot+=valore2
				case "-": valore1_tot-=valore2
				case "*": valore1_tot*=valore2
				case "/": valore1_tot/=valore2
			valore1_tot = self.defTipo(valore1_tot)  # Formatta il risultato finale (es. 5.0 diventa 5).
			output_cronologia = f"{calcolo} {valore1_tot}"
			print(f"{'-'*29}")
			print(f"{calcolo}\n{valore1_tot}\n")
			self.cronologia.append(output_cronologia)

if __name__=="__main__":
	calcolatrice = Calcolatrice()
	calcolatrice.esegui()