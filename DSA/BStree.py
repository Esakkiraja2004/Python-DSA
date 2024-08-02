class node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self,value):

        new_node = node(value)
        if self.root is None:
            self.root = new_node
            return True 
        temp = self.root
        while True:

            if new_node.value ==  temp.value:
                return False

            if new_node.value < temp.value:

                if temp.left is None:
                    temp.left = new_node            
                    return True   
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node            
                    return True   
                temp = temp.right

    def contains(self,value):

        if self.root is None:
            return False
        temp = self.root
        while temp:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else: # value is equal to temp.value
                return True
        return False


# t = tree()
# t.insert(0)
# t.insert(5)
# t.insert(4)
# print(t.root.value)
# print(t.root.left.value)
# print(t.root.right.value)
my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(18)
my_tree.insert(50)
my_tree.insert(17)
my_tree.insert(20)

"""
    THE LINES ABOVE CREATE THIS TREE:
                 2
                / \
               1   3
"""


print('Root:', my_tree.root.value)            
print('Root->Left:', my_tree.root.left.value) 
print('Root->Right:', my_tree.root.right.value)   
print('Root->Left:', my_tree.root.left.left.value) 
print('Root->Right:', my_tree.root.left.right.value)   

print(my_tree.contains(20))


