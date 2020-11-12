import random
a = map(int,(map(lambda x : random.random()*100 , [None]*10)))
print a

n = len(a)
for k in xrange(n):
	i = k
	j = i-1
	while j>=0 and a[j] > a[i]:
		a[i],a[j] = a[j],a[i]
		j-=1
		i-=1
print a