class Arith_Spoj(object):
	""" 
	Arith_Spoj
	URL : http://www.spoj.com/problems/ARITH/
	"""

	def __init__(self,*args,**kwargs):
		pass

	def basic(self,n,sign):
		task =""
		for i in xrange(n):
			task+=sign
		return task

	def createLine(self,n):
		return self.basic(n,'-')

	def addSpace(self,n):
		return self.basic(n,' ')

	def length(self,a,b,c):
		l1 = len(a);l2 = len(b) ;l3 = len(c)
		n = max(l1,l2,l3)
		return (n,l1,l2,l3)

	def format(self,a,b,c):
		n,l1 ,l2 ,l3 = self.length(a,b,c)	
		a = self.addSpace(n-l1)+a
		b = self.addSpace(n-l2)+b
		c = self.addSpace(n-l3)+c
		return a+"\n"+b+"\n"+self.createLine(n)+"\n"+c+"\n"

	def multiply_format(self,a,b,c):
		mini_ans = []
		old_a = long(a)
		old_b = b[1:]
		n,l1 ,l2 ,l3 = self.length(a,b,c)	

		a = self.addSpace(n-l1)+a
		mini_ans.append(a)
		
		b = self.addSpace(n-l2)+b
		mini_ans.append(b)

		unit = len(str(long(old_b[-1])*old_a))
		temp_line = self.createLine(max(l2,unit))
		temp_line = self.addSpace(n-len(temp_line))+temp_line
		mini_ans.append(temp_line)

		# if b has length more than 1 character
		if l2 > 2 :
			# for product of each digit
			a = old_a
			b = old_b[::-1]
			space_back = 0
			for each_digit in b :
				temp  = str(a*long(each_digit))+self.addSpace(space_back)
				temp = self.addSpace(n-len(temp)) + temp
				mini_ans.append(temp)
				space_back+=1

			mini_ans.append(self.createLine(n))
		c = self.addSpace(n-l3)+c
		mini_ans.append(c)
		ans = ""
		for i in mini_ans :
			ans = ans+i+"\n"
		return ans


	def returnInt(self,a):
		return (long(a[0]) , long(a[1]))

	def read(self):
		t = long(raw_input())
		self.final_ans = []
		while t:
			t-=1
			s = raw_input()
			if '+' in s :
				s = s.split('+')
				a,b = self.returnInt(s)
				ans = a+b
				self.final_ans.append(self.format(str(a),'+'+str(b),str(ans)))
			elif '-' in s :
				s = s.split('-')
				a,b = self.returnInt(s)
				ans = a-b
				self.final_ans.append(self.format(str(a),'-'+str(b),str(ans)))
			else :
				s = s.split('*')
				a,b = self.returnInt(s)
				ans = a*b
				self.final_ans.append(self.multiply_format(str(a),'*'+str(b),str(ans)))

	def print_output(self):
		a = ""
		for x in self.final_ans :
			a = a +x+"\n"
		print a[:-1]



obj = Arith_Spoj()
obj.read()
obj.print_output()