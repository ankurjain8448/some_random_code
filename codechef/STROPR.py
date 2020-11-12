t = int(raw_input())
mod = 10**9 + 7
while t:
	t-=1
	n,x,m = map(int,raw_input().split())
	arr = map(int,raw_input().split())[:x]
	if x < 3:
		pass
		if x==1:
			print arr[0]
		elif x==2:
			ans = (((m%mod)*(arr[0]%mod))%mod + arr[1])%mod
			print ans
	else :
		print arr[0]
