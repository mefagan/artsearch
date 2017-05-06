import string
def getWordsFromText(text):
	translation_table = string.maketrans(string.uppercase, string.lowercase)
	text = text.translate(translation_table)
	text = "".join(c for c in text if c not in ('!','.',':'))
	words = text.split()
	print("size of words list")
	print(len(words))
	return words