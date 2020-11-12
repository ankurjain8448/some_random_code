def gcd(a,b):
	if b== 0:
		return a
	else :
		return gcd(b,a%b)

while True:
	a,b = map(int,raw_input().split())
	print gcd(a,b)
	pass

# def sort_non_decreasing(arr,n):
# 	extra_balls = 0
# 	if arr[0]==0 :
# 		arr[0]=1

# 	for i in xrange(1,n):
# 		if arr[i-1] > arr[i]:
# 			extra_balls= extra_balls+ (arr[i-1] - arr[i])
# 			arr[i] = arr[i-1]
# 	return arr , extra_balls



# t = int(raw_input().split()[0])
# while t:
# 	t-=1
# 	n = int(raw_input().split()[0])
# 	arr = map(int,raw_input().split())
# 	extra_balls = 0
# 	# arr ,extra_balls = sort_non_decreasing(arr,n)
# 	if arr[0]==0:
# 		arr[0] = 1
# 		extra_balls=1

# 	for i in xrange(1,n):
# 		if arr[i-1]>arr[i]:
# 			extra_balls = extra_balls+ (arr[i-1]-arr[i])
# 			arr[i] = arr[i-1]
# 		gc = gcd(arr[i-1],arr[i])
# 		if gc < 2 :
# 			left = arr[i-1]
# 			right = arr[i]
# 			gc = gcd(left+1,right)
# 			if gc > 1 :
# 				extra_balls+=1
# 				arr[i-1] +=1
# 				break
# 			gc = gcd(left,right+1)
# 			if gc > 1 :
# 				extra_balls+=1
# 				arr[i] +=1
# 				break
# 			gc = gcd(left+1,right+1)
# 			if gc > 1 :
# 				extra_balls+=2
# 				arr[i] +=1
# 				arr[i-1] +=1
# 				break