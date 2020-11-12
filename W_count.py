import sys
class WordCount(object):
	"""docstring for WordCount"""
	def __init__(self, arg):
		self.count = 0
		self.d = {}
		self.files = arg		

	def function(self,file_name) :
		with open(file_name) as f :
			temp = f.readline()
			while temp :
				temp =  temp.split()
				for i in temp :
					i.strip("\n\t\r") 
					i.replace("\t","").replace("\r","")
					if len(i) and i!=" ":
						self.count +=1
						if i in self.d :
							self.d[i]+=1
						else :
							self.d[i] =1
				temp = f.readline()

	def worker(self):
		temp=[]
		# checking if files exists or not
		for file_name in self.files :
			try : 
				f = open(file_name)
				f.close()
				temp.append(file_name)
			except :
				print "'%s' file is not present" % (file_name)

		for file_name in temp :
			self.function(file_name)

	def print_Data(self):
		print "count : %d " % (self.count)
		print "--------------DATA------------------"
		for key , value in self.d.items() :
			print " %s  : %d" %(key,value)

if __name__ == "__main__" :
	files = sys.argv[1:]
	if type(files) == str :
		files = files.split()
	obj = WordCount(files)
	obj.worker()
	obj.print_Data()