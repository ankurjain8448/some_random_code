class Arith_Spoj(object):
	"""docstring for Arith_Spoj"""
	def __init__(self, *arg, **kwargs):
		pass


	def add_symbol(self,n,sign):
		task =""
		for i in xrange(n):
			task+=sign
		return task

	def core_add(self,a,b):
		len_a,len_b = len(a),len(b)
		if len_b > len_a :
			a,b = b,a

		# here a is greater than b
		len_a,len_b = len(a),len(b)
		# n = max(len_a,len_b)
		carry = 0
		c =""
		while len_b:
			len_b-=1
			len_a-=1
			s = int(a[len_a]) + int(b[len_b])
			s = s+carry
			carry = s/10
			c = str(s%10)+c
		while len_a:
			len_a-=1
			s = int(a[len_a]) + carry
			carry = s/10
			c = str(s%10)+c

		if carry > 0:
			c = str(carry)+c
		return c


	def add(self,a,b='0'):
		
		final_block = []
		final_block.append(a)
		final_block.append('+'+b)
		
		c =self.core_add(a,b)

		line = self.add_symbol(max(len(c) , len(final_block[1])),'-')
		final_block.append(line)
		final_block.append(c)
		l1,l2,l3 = len(final_block[0]),len(final_block[1]),len(final_block[3])
		n = max(l1,l2,l3)
		final_block[0] = self.add_symbol(n-l1,' ') +final_block[0]
		final_block[1] = self.add_symbol(n-l2,' ') +final_block[1]
		final_block[2] = self.add_symbol(n-len(line),' ') +final_block[2]
		final_block[3] = self.add_symbol(n-l3,' ') +final_block[3]
		ans = ""

		for i in final_block :
			ans = ans+i+"\n"
		return ans

	def subtract(self,a,b):
		len_a , len_b= len(a),len(b)
		final_block = []
		final_block.append(a)
		final_block.append('-'+b)
		a = [ int(i) for i in a ]
		b = [ int(i) for i in b ]

		c = ""
		while len_b:
			len_b-=1
			len_a-=1
			x = int(a[len_a])
			y = int(b[len_b])
			if x<y:
				a[len_a-1] = a[len_a-1] - 1
				x = x + 10
			c = str(x-y)+c

		while len_a:
			len_a-=1
			c = str(a[len_a]) + c

		a = final_block[0]
		b = final_block[1]
		c = c
		len_a , len_b, len_c= len(a),len(b) ,len(c)

		n = max(len_b,len_c)
		line = self.add_symbol(n,'-')

		n = max(n,len_a)

		a = self.add_symbol(n- len_a,' ') + a
		b = self.add_symbol(n- len_b,' ') + b
		c = self.add_symbol(n- len_c,' ') + c
		line = self.add_symbol(n- len(line),' ') + line
		ans = a+"\n"+b+"\n"+line+"\n"+c+"\n"
		return ans




	def multiply(self,a,b):
		len_b = len(b)
		addition = ""
		final_block = []
		final_block.append(a)
		final_block.append('*'+b)
		temp_ans = self.multilpy_each_digit(a,b[len_b-1])

		final_block.append(self.add_symbol(max(len(temp_ans),len(final_block[1])),'-'))
		ans = ""
		if len_b>1 :

			for i in xrange(len_b) :
				ans = self.multilpy_each_digit(a,b[len_b-1-i])
				addition = self.core_add(ans + self.add_symbol(i,'0'),addition)
				ans= ans + self.add_symbol(i,' ')
				final_block.append(ans)

			final_block.append(self.add_symbol(max(len(ans),len(addition)),'-'))
			final_block.append(addition)
		else : 
			final_block.append(temp_ans)
		
		l = 0
		for i in final_block :
			l = max(l,len(i))

		for i in xrange(len(final_block)) :
			final_block[i] = self.add_symbol(l-len(final_block[i]),' ') + final_block[i]
			print final_block[i]
		print ""

	def multilpy_each_digit(self,a,b):
		"""
		a = 1234
		b = 5
		Process : 
		    --------------
			|carry : 112
			|		1234
			|		  *5
			|		----
			|		6170

		"""

		b = int(b)
		final_string = []
		if b==0:
			final_string.insert(0,'0')			
		else :
			len_a = len(a)
			carry = 0
			for i in xrange(len_a):
				a_digit = int(a[len_a-1-i])
				mul = a_digit*b
				mul+=carry
				carry = mul/10
				final_string.insert(0,str(mul%10))

			if carry >0:
				final_string.insert(0,str(carry))
		ans = ""
		for each in final_string :
			ans+=each

		return ans

	def read(self):
		t = int(raw_input())
		while t:
			t-=1
			s = raw_input()
			if '+' in s:
				a,b = s.split('+')
				print self.add(a,b)
			elif '-' in s :
				a,b = s.split('-')
				ans = self.subtract(a,b)
				print ans
			else :
				a,b = s.split('*')
				self.multiply(a,b)
				


obj = Arith_Spoj()
obj.read()