class BinarySearchTreeNode:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

def add_child(self,data):
    if data==self.data:
        return
    if data<self.data:
        #add the data in the left subtree
           if self.left: # you are not leaf node
                self.left.add_child(data)
           else:
                self.left=BinarySearchTreeNode(data)
    else:
        #add data to right subtree
        self.right=BinarySearchTreeNode(data)

def in_order_traversal(self):
#visit left subtreee
     elements=[]
     if self.left:
          elements+=self.left.in_order_traversal()
        #visit base node
          elements.append(self.data)
    #visit right subtreee
          elements+=self.right.in_order_traversal()
          return elements
def bulid_tree(elements):
     root=BinarySearchTreeNode(elements[0])
     for i in range(1,len(elements)):
          root.add_child(elements[i])
          return root
if __name__=='__main__':
     numbers=[1,2,3,4,5,6]
numbers_tree=bulid_tree(numbers)
print(numbers_tree.in_order_traversal())
     


   

        