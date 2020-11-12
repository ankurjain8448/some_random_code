# include <iostream>
using namespace std;

typedef struct node{
    int val;
    struct node* left;
    struct node* right;
    int ht;
} node; 

node * newNode(int val){
   struct node *temp  = new node ;
    temp->val = val;
    temp->left = NULL;
    temp->right = NULL;
    temp->ht = 0 ; 
    return temp;
}


int get_height(node *root){
    int ans = -1;
    if ((root->left) && (root->right))
        ans =  max(root->left->ht,root->right->ht) ;
    if ((root->left==NULL) && (root->right)) 
      ans = root->right->ht; 
    if ((root->left) && (root->right == NULL))
      ans =  root->left->ht ;
    ans++;
    return ans; 
}


int balance_factor(struct node * root){
    if ((root->left==NULL) && (root->right == NULL))
        return 0 ;
    if ((root->left==NULL) && (root->right)) 
      return -root->right->ht-1; 
    if ((root->left) && (root->right == NULL))
      return root->left->ht +1 ;
    return root->left->ht - root->right->ht;
}


node * LL_rotation(node * root){
  struct node *temp  = root->left ;
  root->left = temp->right;
  temp->right = root;
  root->ht = get_height(root);
  temp->ht = get_height(temp);
  return temp ;
}

node * LR_rotation(node * root){
  struct node * temp = root->left ;
  struct node * x = temp->right ;
  root->left = x;
  temp->right = x->left ;
  x->left = temp;
  temp->ht = get_height(temp);
  x->ht = get_height(x);
  root->ht = get_height(root);
  return LL_rotation(root);
}


node * RR_rotation(node * root){
  struct node * temp = root->right;
  root->right = temp->left;
  temp->left= root;
  root->ht = get_height(root);
  temp->ht = get_height(temp);
  return temp;
}

node * RL_rotation(node * root){
  struct node * temp = root->right;
  struct node * x = temp->left;
  root->right = x;
  temp->left = x->right;
  x->right = temp;
  temp->ht = get_height(temp);
  x->ht = get_height(x);
  root->ht = get_height(root);
  return RR_rotation(root);
}


node * do_something(node * root){
  int factor = balance_factor(root);
  if (factor>1){
     // factor is 2
    int child_factor = balance_factor(root->left);
    if (child_factor == 1 ){
      root = LL_rotation(root);
    }
    else if (child_factor == -1){
      root = LR_rotation(root);
    }
  }
  if (factor < -1){
    // factor is -2
    int child_factor = balance_factor(root->right);
    if (child_factor == 1 ){
      root = RL_rotation(root);
    }
    else if (child_factor == -1){
      root = RR_rotation(root);
    }
  }
  return root ;
}

bool search(node * root , int val){
  bool ans  = false;
  if(root){
    if (root->val == val)
      return true;
    else if (val > root->val)
      ans = search(root->right, val);
    else 
      ans = search(root->left, val);
    }
  return ans;
}

int del_doing_right(node * root, node* par){
  if(root->left){
    int val = del_doing_right(root->left,root);
    root->ht = get_height(root);
    root = do_something(root);
    return val;
  }
  else {
    int val = root->val;
    par->left = NULL;
    return val;
  }
}

node* del(node * root , int val ,node * par){
    if (root->val == val){
          if (root->right){
                par = root;
                root = par->right;
                if(root->left)
                    par->val = del_doing_right(root->left, root);
                else{
                  par->val = root->val;
                  par->right = root->right;                  
                }
                  
                root = par;
                root->ht = get_height(root);
                root = do_something(root);  
              }
          else if(root->left){
              // one child i.e left
              if(par){
                par->left = root->left;
                root = par->left;
              }
              else {
                root->val = root->left->val;
                root->left = NULL;
              }
            root->ht = get_height(root);
          root = do_something(root);      
          } 
          else 
            root = NULL;
          
          return root;
    }
    else if (val > root->val)
      {
        cout << "going in right subtree "<<endl;
        root->right = del(root->right, val, root);
        root->ht = get_height(root);
        root = do_something(root);
      }      
      else {
        cout << "going in left subtree "<<endl;
        root->left = del(root->left, val, root);
        root->ht = get_height(root);
        root = do_something(root);
      }   

  return root;
}

node * insert(node * root,int val){
   if (root){
      if(val==root->val)
        return root ;
       if (val > root->val){
           root->right = insert(root->right,val);
       }
       else {
           root->left = insert(root->left,val);
       }
        root->ht = get_height(root);
        root = do_something(root);
   }
    else {
        struct node * t = newNode(val);
        return t;
    }
   return root;
}

void inorder(node* root){
  if(root){
    inorder(root->left);
    cout << root->val << "("<<root->ht<<")"<< " --> ";
    inorder(root->right);
  }
  return ;
}

void preorder(node* root){
  if(root){
    cout << root->val << "("<<root->ht<<")"<< " --> ";
    preorder(root->left);    
    preorder(root->right);
  }
  return ;
}

int main(void){
   int N , val,nodes;
   char char_temp;
   struct node * root = NULL ;

   cin >> N;
   nodes = 0;
   for(int i = 0; ; i++){
      
      cin >> char_temp >> val;

      if (char_temp== 'a') {
        root = insert(root,val);
        nodes++;        
      }
      else if (char_temp== 'd') {
            bool is_present = search(root, val);
            // cout <<"is_present : "<<is_present<<endl;
            if (is_present){
              root = del(root, val,NULL);
              nodes--;
            }
            else 
              cout << "Wrong ! node is not present"<<endl;
        }
        else if (char_temp== 'p') {
              inorder(root);
              cout <<endl<<"preorder "<< endl;
              preorder(root);
              cout << endl;
           }
        else 
          break;
      }
      // calculate median [-1,0,1]        
   
   inorder(root);
   cout <<endl<<"preorder "<< endl;
   preorder(root);
   return 0;
}