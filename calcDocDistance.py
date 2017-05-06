#Taken and adapted from MIT lectures at https://courses.csail.mit.edu/6.006/fall11/rec/rec02.pdf
import math
from insertionSort import insertion_sort
from innerProduct import inner_product
from readFile import read_file
from mergeSort import merge_sort
from getWordsFromText import getWordsFromText

def countFrequency(wordList):
	#document vector
	dictionary = {}
	#looks up each word in the wordlist
	for word in wordList:
		#goes through each word and checks to see if it's in the list
		if word in dictionary:
			#if it's in the list then it increments the count by one
			dictionary[word] = dictionary[word] +1
		else:
			dictionary[word] = 1
			
	return dictionary

def getWordFrequency(filename):
	text = read_file(filename)
	words = getWordsFromText(text)
	frequencyMap = countFrequency(words)
	return frequencyMap

def calculateVectorAngle(L1, L2):
	numberator = inner_product(L1, L2)
	#distance metric
	denominator = math.sqrt(inner_product(L1, L1) * inner_product(L2, L2))
	if denominator==0:
		return float('inf')
	return math.acos(numberator/denominator)

def calculateDistance(filename1, filename2):
	sortedWordList1 = getWordFrequency(filename1)
	sortedWordList2 = getWordFrequency(filename2)
	distance = calculateVectorAngle(sortedWordList1, sortedWordList2)
	return distance
	

	
	
