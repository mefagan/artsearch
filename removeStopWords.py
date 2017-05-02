#code adapted from http://stackoverflow.com/questions/19560498/faster-way-to-remove-stop-words-in-python
import sys
import os

def stripStopWords(text, i):
	#print(text)
	#testtext = "hi the me the bicycle maryeileen a the them hi"
	with open('stop_words.txt', 'r') as myfile:
		data=myfile.read()

	stop_words = data.split()
	#print(testtext)
	#print(stop_words)

	#text = text.decode('unicode_escape').encode('ascii','ignore')
	#tokenized_text = word_tokenize(text)
	#print(tokenized_text)
	clean_text = ' '.join([word for word in text.lower().split() if word not in stop_words])
	#print(clean_text)
	#print(clean_text)
	#path = 'noStopWords_files'
	#if not os.path.exists(path):
	#	os.makedirs(path)
	#f = str(i)
	#clean_text.decode('utf-8')
	#with open(os.path.join(path, f), 'wb') as temp_file:
	#	temp_file.write(clean_text)
	return clean_text

def main():
	path = 'strippedHTML_files'
	i = 0 
	for filename in os.listdir(path):
		with open(os.path.join(path, filename), 'r') as myfile:
			
			data=myfile.read()
			data = str(data)
			stripStopWords(data, i)
			i = i+1
if __name__ == '__main__':
	main()