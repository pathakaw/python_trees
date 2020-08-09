# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 16:06:48 2019

@author: AWADHESH
"""

class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left
        
class BinaryTree(object):
    def __init__(self, root=None):
        self.root = Node(root)
        
def preOrderSearch(root, value):

    if root is not None:
        if root.value == value:
            print("Value Found")
            return True
        preOrderSearch(root.left, value)
        preOrderSearch(root.right, value)
    
    print("Value not found in Tree")
    return False

def preOrderPrint(root, trav=''):
    
    if root is not None:
        trav += (str(root.value) + "-")
        trav = preOrderPrint(root.left, trav)
        trav = preOrderPrint(root.right, trav)
        
    return trav

def InOrderPrint(root):
    if root is not None:
        InOrderPrint(root.left)
        print(root.value)
        InOrderPrint(root.right)
    
def postOrderPrint(root):
    if root is not None:
        postOrderPrint(root.left)
        postOrderPrint(root.right)
        print(root.value)
        

tree = BinaryTree(10)
tree.root.left = Node(20)
tree.root.right = Node(30)
tree.root.right.left = Node(40)
tree.root.right.right = Node(50)

print(preOrderPrint(tree.root))
#preOrderSearch(tree.root, 50)
#InOrderPrint(tree.root)
#postOrderPrint(tree.root)
#tree.add(n1)
#print(tree.root.value)


        
        