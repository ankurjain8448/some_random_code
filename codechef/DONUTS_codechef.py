def solve(a,m):
	a = sorted(a)
	flag = True
	ans = 0
	can_connect = 0
	i = 0
	while flag:
		can_connect =  a[i]*2
		if (m-1) == can_connect :
			ans+=a[i]
			flag = False
		else :
			if (m-1) > can_connect:
				ans+=a[i]
				m -=can_connect
				i+=1
			else :
				temp = (m-1)/2
				ans = ans + temp + 1
				a[i]-=temp
				flag = False
	return ans

t = int(raw_input())
while t:
	t-=1
	n , m = map(int,raw_input().split())
	a = map(int,raw_input().split())
	print solve(a,m)