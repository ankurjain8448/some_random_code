a = [2,4,7,5,1,3]
n = len(a)
total_nodes = 2*n-1
seg_tree = [total_nodes]*0

# par = (i-1)/2
# lchild = 2*i + 1
# rchild = 2*i + 2
start = 0
end = total_nodes -1
mid  = 0

def get_mid(start,end):
	return (start+end)/2

def create_segment_tree(a,seg_tree,start,end,mid,sum):
	if start > end :
		mid = get_mid(start,end)
		return create_segment_tree(a,seg_tree,start,end,mid,sum):
		return create_segment_tree(a,seg_tree,start,end,mid,sum):

create_segment_tree(a,seg_tree,start,end,mid,sum)
