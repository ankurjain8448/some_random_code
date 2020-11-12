n = int(raw_input())
d = {}
l = []
while n:
	n-=1
	name = raw_input()
	marks = float(raw_input())
	if marks not in l :
		l.append(marks)
	if marks not in d :
		d[marks] = [name]
	else :
		d[marks].append(name)

m = min(l)
temp  = [ i for i in l if i!=m ]
m = min(temp)
a = d[m]
a.sort()
for i in a:
    print i