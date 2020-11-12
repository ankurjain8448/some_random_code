t = int(raw_input())
while t:
	t-=1
	n = int(raw_input())
	keys = {}
	for each_row in xrange(n):
		row = each_row+1
		col = 1
		for i in raw_input().split():
			keys[int(i)] = (row,col)
			col+=1

	ans = 0
	for i in xrange(2,n**2+1):
		cur_x,cur_y = keys[i]
		prev_x,prev_y = keys[i-1]
		ans = ans + abs(cur_x - prev_x) + abs(cur_y - prev_y)

	print ans
		