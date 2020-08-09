# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 00:59:38 2019

@author: AWADHESH
"""

class BinaryHeap(object):
    def __init__(self):
        self.heap_list =[0]
        self.current_size = 0
        
    def minChild(self, i):
        if (i * 2) + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[2 * i] < self.heap_list[ (2 * i) + 1]:
                return 2 * i
            else:
                return (2 * i) + 1
        
    def precolateUp(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2 ]:
                self.heap_list[i], self.heap_list[i // 2 ] = self.heap_list[i // 2], self.heap_list[i]
            i = i // 2   
            
    def percolateDown(self, i):
        while (i * 2) <= self.current_size:
            mc = self.minChild(i)
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc]= self.heap_list[mc], self.heap_list[i]
            i = mc
            
    def insert(self, k):
        self.heap_list.append(k)
        self.current_size = self.current_size + 1
        self.precolateUp(self.current_size)
        
    
    def delMin(self):
        last_element = self.heap_list.pop()
        deleted = self.heap_list[1]
        self.heap_list[1] = last_element
        self.current_size = self.current_size - 1
        self.percolateDown(1)
        return deleted

bh = BinaryHeap()
bh.insert(30)
bh.insert(20)
bh.insert(10)
bh.insert(5)
print(bh.delMin())
print(bh.heap_list)
