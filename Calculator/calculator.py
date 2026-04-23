class Calculator:
	def __init__(self):
		self.history: list[str] = []  # Type hint: specifies that "history" is a list of strings.

	def defType(self, number: float) -> int | float:
		if number.is_integer():
			return int(number)
		return number

	def manageControls(self, control: str) -> bool:
		match control.strip().lower():  # Lower cases the input and removes lateral spaces.
			case "help":
				print("\n<<To view history enter \"cronos\", to clear it enter \"c_cronos\"; type \"x\" to exit the program.>>\n")
				return True
			case "cronos":
				if self.history:  # Checks if there is history.
					print(f"\n{'*'*34}\nHistory:")
					for i in self.history:
						print(i)
					print(f"{'*'*34}\n")
				else:
					print("History is empty.\n")
				return True
			case "c_cronos":
				if self.history:
					self.history.clear()
					print("History cleared.\n")
				else:
					print("No history to clear.\n")
				return True
			case "x" | "X":
				print("\nClosing calculator...\n")
				exit()  # Cleanly closes the program.
			case _:
				return False  # If none of the above controls is matched, return "False".

	# Method for validating number input
	def checkNumber(self, input_text: str) -> int | float:
		while True:
			value = input(input_text).strip()
			if self.manageControls(value):
				continue  # If a command is called, skip casting and repeat number input.
			try:
				number = float(value)  # Try casting to float.
				return self.defType(number)
			except ValueError:
				print("Error: invalid input. Input exclusively a number or a command.\n")

	# Method for validating operation input
	def checkOp(self, input_text: str) -> str:
		valid_ops = ["+", "-", "*", "/"]
		while True:
			op = input(input_text).strip()
			if self.manageControls(op):
				continue  # If a command is called, skip check and repeat operation input.
			if op in valid_ops:  # Checks if the selected operation is included in the list of valid operations.
				return op
			else:
				print("Error: invalid input. Input exclusively one of: [+, -, * (multiplication), / (division)] or a command.\n")

	def execute(self):
		TEXT1, OP_TEXT, TEXT2="Enter a number:\n", "Choose an operation [+, -, * (multiplication), / (division)]:\n", "Enter a second number:\n"
		print("\nCALCULATOR - (type \"help\" to view the controls, \"x\" to exit the program)\n\n0")
		
		while True:
			value1_tot = self.checkNumber(TEXT1)
			op = self.checkOp(OP_TEXT)
			while True:
				value2 = self.checkNumber(TEXT2)
				if op == "/" and value2 == 0:
					print("You cannot divide by 0!\n")
				else:
					break  # Ends the division check and proceeds to calculation.
			calculation = f"{value1_tot} {op} {value2} ="
			match op:
				# The result of the calculation is stored in the same variable that once stored the first number.
				case "+": value1_tot+=value2
				case "-": value1_tot-=value2
				case "*": value1_tot*=value2
				case "/": value1_tot/=value2
			value1_tot = self.defType(value1_tot)  # Formats the final result (e.g. 5.0 becomes 5).
			output_history = f"{calculation} {value1_tot}"
			print(f"{'-'*29}")
			print(f"{calculation}\n{value1_tot}\n")
			self.history.append(output_history)

if __name__=="__main__":
	calculator = Calculator()
	calculator.execute()