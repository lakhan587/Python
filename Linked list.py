#!/usr/bin/env python
# coding: utf-8

# In[2]:


#linked list in python 
class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
        
class LinkedList:
    def __init__(self):
        self.head=None
        
    def insert_at_begining(self,data):
        node=Node(data,self.head)
        self.head=node
        
    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        
        while itr:
            llstr +=str(itr.data) + '---->' 
            itr = itr.next
            
        print(llstr)
        
        
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        
        itr = self.head
        
        while itr.next:
            itr = itr.next
            
        itr.next = Node(data,None)    
    
    def insert_value(self,data_list):
        self.head=None
        
        for data in data_list:
            self.insert_at_end(data)
    
    def get_length(self):
        count=0
        itr=self.head
        
        while itr:
            count+=1
            itr = itr.next
            
        return count    
    
    def remove_At(self,index):
        if index<0 or index>= self.get_length():
            raise Exception('Invalid index')
            
        if index==0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
                
            itr = itr.next
            count +=1
            
            
    def insert_at(self,data,index):
        if index<0 or index>=self.get_length():
            raise Exception('Invalid Index')
            
        if index == 0:
            self.insert_at_begining(data)
            
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node =Node(data,itr.next)
                itr.next=node
            
            itr =itr.next
            count+=1
            
    def find_position(self,data):
        itr = self.head
        count = 0
        while itr:
            if itr.data == data:
                return count
            itr = itr.next
            count +=1
        
        
        
    def insert_after_value(self,data_after,data_to_insert):
        pos = self.find_position(data_after)
        if pos:
            self.insert_at(data_to_insert,pos+1)
            
    def remove_by_value(self,data):
        pos = self.find_position(data)
        if pos!=None:
            self.remove_At(pos)
        else:
            print('{} is not found in linked list'.format(data))
    
if __name__ == '__main__':
    ll =LinkedList()
#     ll.insert_at_begining(5)
#     ll.insert_at_begining(89)
#     ll.insert_at_begining(42)
#     ll.insert_at_e
    ll.insert_value(["banana","mango","grapes","orange"])
    ll.print()
    print("Length of linkedList is :",ll.get_length())
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print()
    print("Length of linkedList is :",ll.get_length())
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()

