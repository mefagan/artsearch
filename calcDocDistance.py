#Taken and adapted from MIT lectures at https://courses.csail.mit.edu/6.006/fall11/rec/rec02.pdf
import math

def read_file(filename):
	with open(filename, 'r') as myfile:
		line_list=myfile.read().splitlines()
	return line_list

def getWordsFromLineList(line_list):
	words = []
	for line in line_list:
		words_in_line = getWordsFromString(line)
		words = words + words_in_line
	return words

def getWordsFromString(line):
	wordList = []
	characterList = []
	#check if each character is alphanumeric and append if yes, or end word and append word if no
	for c in line:
		if c.isalnum():
			characterList.append(c)
		elif len(characterList) > 0:
			word = "".join(characterList)
			word = word.lower()
			characterList = []
	#if you make it through the line then add the word to the word list
	if len(characterList)>0:
		word = "".join(characterList)
		word = word.lower()
		wordList.append(word)
	return wordList

def countFrequency(wordList):
	#document vector
	list = []
	#looks up each word in the wordlist
	for word in wordList:
		#goes through each word and checks to see if it's in the list
		for entry in list:
			#if it's in the list then it increments the count by one
			if word == entry[0]:
				entry[1] = entry[1] + 1
				break
		else:
			list.append([word, 1])
	return list

def getWordFrequency(filename):
	line_list = read_file(filename)
	words = getWordsFromLineList(line_list)
	frequencyMap = countFrequency(words)
	return frequencyMap

def inner_product(L1, L2):
	sum = 0.0
	for word1, count1 in L1:
		for word2, count2 in L2:
			if word1==word2:
				sum += count1 * count2
	return sum

def calculateVectorAngle(L1, L2):
	numberator = inner_product(L1, L2)
	#distance metric
	denominator = math.sqrt(inner_product(L1, L1) * inner_product(L2, L2))
	return math.acos(numberator/denominator)

def calculateDistance(filename1, filename2):
	sortedWordList1 = getWordFrequency(filename1)
	sortedWordList2 = getWordFrequency(filename2)
	distance = calculateVectorAngle(sortedWordList1, sortedWordList2)
	print(distance)

	
	
