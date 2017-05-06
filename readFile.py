def read_file(filename):
	with open(filename, 'r') as myfile:
		data=myfile.read()
	return data