t = int(raw_input())
main_arr = [1]
def power_a_b(a, b):
	if b == 1:
		return a
	else :
		if b%2 == 0:
			return power_a_b(a**2,b/2)
		else:
			return a*power_a_b(a**2,(b-1)/2)


def preprocess(n, mod):
	for i in xrange(1,mod):
		ans = power_a_b(j, j)%mod
		ans = (ans*main_arr[i-1])%mod
		main_arr.append(ans)
	
	for i in xrange(mod,n+1):
		main_arr.append(0)


def gcd(a, b):
	if b == 1:
		return a
	else:
		return gcd(b, a%b)

def a_minus_b_mod(a, b, m):
	return (a%m - b%m + m )%m


def a_divide_b_mod(a, b, m):
	ans = ((a%m)*(gcd(b, m)))%m
	return ans

while t:
	t -= 1
	main_arr = [1]
	n, mod, q = map(int, raw_input().split())
	preprocess(n, mod)
	for i in q:
		r = int(raw_input())
		ans = a_minus_b_mod(r, n-r, mod)
		temp_ans = a_divide_b_mod(n, ans, mod)
		print temp_ans
	main_arr = None