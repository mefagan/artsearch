from tidylib import tidy_document

def parsehtml(data):
	document, errors = tidy_document(data, options=None, keep_doc=False)
	return document, errors

	
