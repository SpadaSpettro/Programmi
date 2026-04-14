# Funzioni comandi
def comandi(input_utente, testo_input):
	while input_utente=="help":
		print("\n<<Per visualizzare la cronologia scrivi 'cronos', per cancellarla scrivi 'c_cronos'.>>\n")
		input_utente=input(testo_input)
	input_utente=vedi_cronologia(input_utente, testo_input)
	input_utente=cancella_cronologia(input_utente, testo_input)
	return input_utente

def vedi_cronologia(input_utente, testo_input):
	while input_utente=="cronos":
		if len(cronologia_list)>0:
			print(f"\n{'*'*34}\nCronologia:")
			for i in cronologia_list:
				print(i)
			print(f"{'*'*34}\n")
		else:
			print("Nessuna cronologia.\n")
		input_utente=input(testo_input)
		input_utente=comandi(input_utente, testo_input)
		input_utente=cancella_cronologia(input_utente, testo_input)
	return input_utente

def cancella_cronologia(input_utente, testo_input):
	while input_utente=="c_cronos":
		if len(cronologia_list)>0:
			cronologia_list.clear()
			print("Cronologia cancellata.\n")
		else:
			print("Nessuna cronologia da cancellare.\n")
		input_utente=input(testo_input)
		input_utente=comandi(input_utente, testo_input)
		input_utente=vedi_cronologia(input_utente, testo_input)
	return input_utente

# Funzione casting
def def_tipo(x):
	if float(x)-int(float(x))==0:
		x=int(float(x))
	else:
		x=float(x)
	return x

# Funzione per validare l'input numerico
def richiedi_numero(testo_input):
	while True:
		valore = input(testo_input) # 1. Chiediamo l'input all'utente
		valore = comandi(valore, testo_input) # 2. Passiamo l'input alla funzione comandi (gestisce "help", "cronos", ecc.)
		try: # 3. Ora controlliamo se ciò che è rimasto è davvero un numero
			float(valore) # Proviamo a convertirlo in float. Se ha successo, è un numero valido!
			return valore # Restituiamo il valore e usciamo dalla funzione
		except ValueError:
			# Se Python rileva un errore di conversione, stampiamo un messaggio e il ciclo riparte
			print("Errore: inserimento non valido. Devi inserire esclusivamente un numero o un comando.\n")

# Funzione per validare l'input delle operazioni
def richiedi_operazione(testo_input):
	operazioni_valide = ["+", "-", "*", "/"] # Definiamo quali sono le operazioni accettate
	while True:
		operazione = input(testo_input) # 1. Chiediamo l'input
		operazione = comandi(operazione, testo_input) # 2. Passiamo l'input ai comandi
		if operazione in operazioni_valide: # 3. Controlliamo se è una delle 4 operazioni consentite
			return operazione # È valida, usciamo dalla funzione
		else:
			print("Errore: inserimento non valido. Inserisci solo [+, -, * (moltiplicazione), / (divisione)] o un comando.\n")


if __name__=="__main__":
	cronologia_list=[]
	TESTO1, TESTO_OPERAZIONE, TESTO2="Inserisci un numero:\n", "Scegli un'operazione [+, -, * (moltiplicazione), / (divisione)]:\n", "Inserisci un altro numero:\n"
	print("\nCALCOLATRICE\n(digita 'help' per visualizzare i comandi della cronologia)\n\n0\n")
	while True:
		valore1_tot=richiedi_numero(TESTO1)
		valore1_tot=def_tipo(valore1_tot)

		operazione=richiedi_operazione(TESTO_OPERAZIONE)

		valore2=richiedi_numero(TESTO2)
		valore2=def_tipo(valore2)
		
		while (valore2==0 and operazione=="/"):
			print("Non puoi dividere per 0!")
			valore2=richiedi_numero(TESTO2)
			valore2=def_tipo(valore2)
		testo=f"{valore1_tot} {operazione} {valore2} ="
		match operazione:
			case "+":
				valore1_tot+=valore2
			case "-":
				valore1_tot-=valore2
			case "*":
				valore1_tot*=valore2
			case "/":
				valore1_tot/=valore2
		valore1_tot=def_tipo(valore1_tot)
		output=(f"{testo} {valore1_tot}")

		print(f"{'-'*29}")
		print(f"{testo}\n{valore1_tot}\n")
		cronologia_list.append(output)