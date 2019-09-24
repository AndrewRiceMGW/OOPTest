#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 12:34:55 2019

@author: andrew
"""

class Queue:
    def __init__(self, head=None):
        self.storage = list()
    def enqueue(self, new_element):
        self.storage.insert(0, new_element)

    def peek(self):
        return self.storage[0]

    def dequeue(self):
        return self.storage.pop()
    
# Setup
q = Queue(1)
q.enqueue(2)
q.enqueue(3)

# Test peek
# Should be 1
print( q.peek())

# Test dequeue
# Should be 1
print( q.dequeue())

# Test enqueue
q.enqueue(4)
# Should be 2
print( q.dequeue())
# Should be 3
print( q.dequeue())
# Should be 4
print( q.dequeue())
q.enqueue(5)
# Should be 5
print( q.peek())