def read_file(filename):
	with open(filename, 'r') as myfile:
		data=myfile.read()
	line_list = data.splitlines()
	return line_list