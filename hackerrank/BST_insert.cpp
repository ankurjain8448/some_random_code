/*
Node is defined as 

typedef struct node
{
   int data;
   node * left;
   node * right;
}node;

*/

// iterative
// node * insert(node * root, int value)
// {
//     node * temp = root ;
	
// 	node * new_node = new node ;
// 	new_node->data = value;
// 	new_node->left = NULL;
// 	new_node->right = NULL;
	

// 	if (root){
// 		node * par = new node ;
// 		while (temp){
// 		par = temp;
// 		if (value > temp->data){
// 				temp = temp->right;
// 			} 
// 		else{
// 				temp = temp->left;
// 			}
// 		}
	
	
// 		if (value > par->data){
// 			par->right = new_node ;
// 		}
// 		else {
// 			par->left = new_node ;	
// 		}	
// 	}
// 	else{
// 		root = new_node;
// 	}
	
// return root;
// }



node * insert(node * root, int value)
{
	if (root){
		if (value > root->data){
				root = insert(root->right,value);
			} 
		else{
				root = insert(root->left,value);
			}
	}
	else{
		node * temp = new node ;
		temp->data = value;
		temp->left = NULL;
		temp->right = NULL;
		return temp;	
	}
	
   return root;
}
