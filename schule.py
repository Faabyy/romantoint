def to_float(value):
	try:
		return float(value)
	except (ValueError, TypeError):
		print("Bitte geben Sie eine Zahl ein.")
		return 0

while True:
	s = to_float(input())
	if(s != 0):
		break
	
print(s)
