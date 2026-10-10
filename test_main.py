import unittest

from main import calcInt, isValid


class TestCalcInt(unittest.TestCase):
	def test_beispiele_aus_readme(self):
		self.assertEqual(calcInt("III"), 3)
		self.assertEqual(calcInt("LVIII"), 58)
		self.assertEqual(calcInt("MCMXCIV"), 1994)

	def test_subtraktionspaare(self):
		for s, n in [("IV", 4), ("IX", 9), ("XL", 40), ("XC", 90), ("CD", 400), ("CM", 900)]:
			self.assertEqual(calcInt(s), n)

	def test_grenzen(self):
		self.assertEqual(calcInt("I"), 1)
		self.assertEqual(calcInt("MMMCMXCIX"), 3999)


class TestIsValid(unittest.TestCase):
	def test_gueltig(self):
		for s in ["I", "IV", "LVIII", "MCMXCIV", "MMMCMXCIX"]:
			self.assertTrue(isValid(s), s)

	def test_ungueltig(self):
		for s in ["", "iv", "IIII", "VX", "IC", "MMMM", "ABC", "I V", "MMMDCCCLXXXVIII" + "I"]:
			self.assertFalse(isValid(s), s)

	def test_alle_werte_1_bis_3999_roundtrip(self):
		def to_roman(n):
			teile = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
					(50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
			out = ""
			for wert, sym in teile:
				while n >= wert:
					out += sym
					n -= wert
			return out

		for n in range(1, 4000):
			s = to_roman(n)
			self.assertTrue(isValid(s), s)
			self.assertEqual(calcInt(s), n)


if __name__ == "__main__":
	unittest.main()
