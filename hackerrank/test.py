t = int(raw_input())
def is_valid(n):
	flag = True
	for i in n :
		try:
			t = int(i)
		except Exception, e:
			flag = False
			break
		else:
			if t<0 or t>9 :
				flag = False
				break
	if flag :
		t = int(n[0])
		if t < 4 or t> 6 :
			flag = False
	if flag :
		i = 0
		l = len(n)
		j = i+1
		count = 0
		for i in xrange(l):
			while j<l and n[i]==n[j] :
				count+=1
				j+=1
			if count>3 :
				flag = False
				break
			count = 0
			i = j
	return flag
		
while t:
	t-=1
	n = raw_input()
	l = len(n)
	flag = False
	if '-' in n and l==19:
		n = n.split('-')
		ans = True
		flag = True
		for i in n :
			if len(i)!=4:
				ans = False
				flag = False
				break
		if ans :				
			n = "".join(n)
			flag =  is_valid(n)
	elif '-' not in n and l ==16:
		flag =  is_valid(n)
	if flag :
		print "Valid"
	else :
		print "Invalid"
