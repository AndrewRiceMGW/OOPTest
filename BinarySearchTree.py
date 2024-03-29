#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 13:41:18 2019

@author: andrew
"""

class Node(object):
    def __init__(self, data = None):
        self.data = data
        self.right = None
        self.left = None
class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)
    
    def _insert(self, data, current_node):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert(data, current_node.left)
        elif data > current_node.data:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert(data, current_node.right)
        else:
            print("The Value is already present in Tree.")
    def find(self, data):
        if self.root:
            is_found = self._find(data, self.root)
            if is_found:
                return True
            else:
                return False
        else:
            return None
    def _find(self, data, current_node):
        if data > current_node.data and current_node.right:
            return self._find(data, current_node.right)
        elif data < current_node.data and current_node.left:
            return self._find(data, current_node.left)
        if data == current_node.data:
            return True
        
bst = BinarySearchTree()
bst.insert(4)
bst.insert(2)
bst.insert(8)
bst.insert(5)
bst.insert(10)

print(bst.find(11))

