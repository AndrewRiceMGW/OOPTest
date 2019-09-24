#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 09:43:16 2019

@author: andrew
"""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList(object):
    def __init__(self, head = None):
        self.head = head
    def append(self, new_element):
        current = self.head
        if self.head: # if there is an element
            while current.next:
                current = current.next # current moves to next
            current.next = new_element # current next = new_element 
        else:
            self.head = new_element #if no elements in list new element is head
            
    def get_position(self, position):
        current = self.head
        counter = 1
        if position < 1:
            return None
        while current and counter <= position:
            if counter ==position:
                return current
            current = current.next
            counter+= 1
    def insert(self, new_element, position):
        current = self.head
        counter = 1
        if position > 1:
            while current and counter < position:
                if counter == position -1:
                    new_element = current.next
                    current.next = new_element
                current = current.next
                counter += 1
        elif position ==1:
            new_element.next = self.head
            self.head = new_element
    def delete(self, value):
        current = self.head
        previous = None
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next
        elif current.value != value:
            previous = current
            current = current.next
       """ alternative!!!!
        deleted = self.head
        if self.head;:
            self.head = self.head.next
            deleted.next = None 
        return deleted """
    

e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
print(ll.head.next.next.value)
print(ll.get_position(3).value)

ll.insert(e4, 3)
print(ll.get_position(3).value)

ll.delete(1)
print(ll.get_position(1).value)
