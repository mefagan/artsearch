def read_file(filename):
	with open(filename, 'r') as myfile:
		line_list=myfile.read().splitlines()
	return line_list