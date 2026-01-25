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
		current = value[i]
		match current:
			case 'I':
				if(value.endswith('I')):
					r += 1
				elif(value.startswith('I')):
					r -= 1
			case 'V':
				r += 5
			case 'X':
				r += 10
			case 'L':
				r += 50
			case 'C':
				r += 100
			case 'D':
				r += 500
			case 'M':
				r += 1000
	return r

#Hauptprogramm

s = getInput()

print(calcInt(s))

