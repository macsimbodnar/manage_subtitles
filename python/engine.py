import re, sys

class WriteTranscript:

	def __init__ (self, path): 
		self.path=path

	def convert(self, pdf = False, lesson_title = ''):
		testo_completo=""

		srt_file = open(self.path,'r')

		for line in srt_file:
			linea=line[:-2]

			if re.search('[a-zA-Z]', line[:-1]):
				testo_completo+=" " +linea
				
		
		return testo_completo
			
print (WriteTranscript(sys.argv[1]).convert(True, "ED101_0_1_01"))