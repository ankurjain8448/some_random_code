MAX = 500001
bool_arr = [True]*MAX
arr = [1]*MAX
def preprocess():
	bool_arr[0] = bool_arr[1]=False
	arr[0] = 0
	arr[1] = 0
	i = 2
	while i<MAX:
		temp = i
		if bool_arr[temp]:
			temp+=i
			while temp < MAX:
				bool_arr[temp]= False
				arr[temp]+=i
				temp+=i
		else :
			temp+=i
			while temp < MAX:
				arr[temp]+=i
				temp+=i
		i+=1

preprocess()
t = int(raw_input())
while t:
	t-=1
	print arr[int(raw_input())]