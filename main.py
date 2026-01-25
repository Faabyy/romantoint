#Funktionen

def getInput():
	i = 'a'
	i.strip()
	while i == 'a':
		i = input("Geben Sie eine romanische Zahl ein (max 15 Zeichen): " )
		if(i.isalpha() & i.isupper() & isRoman(i) & len(i) <= 15):
			return i
		else:
			print("Bad input")
			i = 'a'

def isRoman(value):
	valid_chars = "IVXLCDM"
	for i in value:
		if i not in valid_chars:
			return False
	return True

def calcInt(value):
	r = 0
	for i in value:
		match value:
			case 'I':
				
			case 'V':
				
			case 'X':
				
			case 'L':
				
			case 'C':
				
			case 'D':
				
			case 'M':
				

#Hauptprogramm

s = getInput()

print(s)

