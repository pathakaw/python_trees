# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 00:18:37 2019

@author: AWADHESH
"""

class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self, item):
        self.data = item
        
    def setNext(self, newnext):
        self.next = newnext
        

class OrderedList(object):
    def __init__(self):
        self.head = None
        self.count = 0
        
    def size(self):
        return self.count
        
    def isEmpty(self):
        return self.head == None
    
    
    def add(self, item):
        current = self.head
            
        previous = None
        found = False
        
        while current != None and not found:
            if item > current.getData():
                previous = current
                current = current.getNext()
            else:
                found = True
        
        new_node = Node(item)
        if previous == None:
            #new_node.setNext(self.head)
            self.head = new_node
        else:
            previous.setNext(new_node)
            new_node.setNext(current)
        
        self.count = self.count + 1
        
        
    def search(self, item):
        current = self.head
        found = False
        
        while current is not None and not found:
            if current.getData() == item:
                found = True
            current = current.getNext()
        
        return found
    
    def remove(self, item):
        current = self.head
        found = False
        previous = None
        
        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        
        if found:
            next_item = current.getNext()
            previous.setNext(next_item)
            self.count = self.count - 1
            
        return 

ol = OrderedList()
ol.add(10)
ol.add(20)
ol.add(30)
ol.add(40)
#ol.add(50)
print(ol.search(10))