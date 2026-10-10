import re

#Funktionen

WERTE = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

# Gueltige roemische Zahl im Bereich 1-3999 (inkl. Subtraktionsregeln)
MUSTER = re.compile(r"M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})")

def getInput():
	while True:
		i = input("Geben Sie eine romanische Zahl ein (max 15 Zeichen): ").strip()
		if isValid(i):
			return i
		print("Bad input")

def isRoman(value):
	valid_chars = "IVXLCDM"
	for i in value:
		if i not in valid_chars:
			return False
	return True

def isValid(value):
	return (0 < len(value) <= 15
		and value.isalpha()
		and value.isupper()
		and isRoman(value)
		and MUSTER.fullmatch(value) is not None)

def calcInt(value):
	r = 0
	for pos, zeichen in enumerate(value):
		wert = WERTE[zeichen]
		# Steht ein groesserer Wert direkt dahinter, wird subtrahiert (z.B. IV, CM)
		if pos + 1 < len(value) and wert < WERTE[value[pos + 1]]:
			r -= wert
		else:
			r += wert
	return r

#Hauptprogramm

if __name__ == "__main__":
	s = getInput()
	print(calcInt(s))
