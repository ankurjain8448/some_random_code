def compare_string(a,b):
	'''check if a > b or not'''
	if a == b :
		return False
	for i in xrange(len(a)):
		if int(a[i]) > int(b[i]) :
			break			
	else :
		return True
	return False

def list_to_str(arr):
	a = ""
	for i in arr :
		a+=i
	return a

def str_to_list(s):
	arr = [ i for i in s ]
	return arr

def create_palin(a):
	l = len(a)
	mid = l/2
	if l%2==0 :
		j = mid ; i = mid -1
	else :
		i = mid -1 ; j = mid + 1
	while i>-1 :
		a[j] = a[i]
		i-=1
		j+=1
	return a

def main_functionality(new_string,i,j):
	_i = i
	for i in xrange(_i,-1,-1) :
		if new_string[i] != '9':
			index = int(new_string[i])
			index+=1
			new_string[i] = str(index)
			new_string[j] = str(index)
			flag = True
			break
		else :
			new_string[i] = '0'
			new_string[j] = '0'
		j+=1
	else :
		new_string.append('1')
		new_string[0] = '1'
		return new_string
	return new_string

t = int(raw_input())
while t:
	t-=1
	old_string = raw_input()
	old_string = str_to_list(old_string)
	new_string = str_to_list(old_string)

	new_string = create_palin(new_string)
	ans = []
	if compare_string(old_string,new_string):
		ans = new_string
	else :
		l = len(old_string)
		mid = l/2
		if l%2==0:
			''' even length string '''
			i = mid -1
			j = mid 
			ans = main_functionality(new_string,i,j)
		else : 
			''' odd length string '''
			i = mid
			j = mid
			ans = main_functionality(new_string,i,j)
	print list_to_str(ans)