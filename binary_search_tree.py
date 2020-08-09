# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 19:52:20 2019

@author: AWADHESH
"""

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

     
class BST(object):
    def __init__(self, root):
        self.root = root
    
    
    def add(self, new_node):
        self.add_element(self.root, new_node)

    def add_element(self, parent, new_node):
            
        if new_node.value < parent.value:
            if parent.left is None:
                parent.left = new_node
            else:
                self.add_element(parent.left, new_node)
                
        elif new_node.value > parent.value:
            if parent.right is None:
                parent.right = new_node
            else:
                self.add_element(parent.right, new_node)
        else:
                print("What the hell")
        
    def search(self, value):
        return self.search_element(self.root, value)
        
    def search_element(self, parent, value):
        
        if parent is not None:
            if parent.value == value:
                return True
            elif value < parent.value:
                print("In left")
                return self.search_element(parent.left, value)
            elif value > parent.value:
                print("In Right")
                return self.search_element(parent.right, value)
            else:
                return False
        return False
    
    
        
    

bst = BST(Node(9))
bst.add(Node(6))
bst.add(Node(16))
bst.add(Node(15))
            
        
#bst = BST(Node(10))
#bst.add(Node(9))
#bst.add(Node(8))
#bst.add(Node(7))
#bst.add(Node(6))
#bst.add(Node(11))
#bst.add(Node(12))

#print(bst.search(9))
#print(bst.search(13))
#print("=========")
print(bst.root.value)
print(bst.root.left.value)
print(bst.root.right.value)
print(bst.root.right.left.value)
#print(bst.root.left.left.value)
#print(bst.root.left.left.left.value)

        