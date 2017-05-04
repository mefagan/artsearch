#Taken and adapted from MIT lectures at https://courses.csail.mit.edu/6.006/fall11/rec/rec02.pdf
import math
from insertionSort import insertion_sort
from innerProduct import inner_product
from readFile import read_file

def getWordsFromLineList(line_list):
	words = []
	for line in line_list:
		words_in_line = getWordsFromString(line)
		words.extend(words_in_line)
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
	insertion_sort(frequencyMap)
	return frequencyMap

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

	
	
