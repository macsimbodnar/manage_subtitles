#!/usr/bin/python

import re, sys

class WriteTranscript:

	def __init__ (self, path): 
		self.path=path

	def convert(self, lesson_title = ''):
		testo_completo=""

		srt_file = open(self.path,'r')

		for line.decode('utf-8') in srt_file:
			linea=line[:-2]

			if re.search('[a-zA-Z]', line[:-1]):
				testo_completo+=" " +linea
				
		
		return testo_completo
			
result = WriteTranscript(sys.argv[1]).convert()

print (result)