# Created By Ken Saetern September 10, 2017

#name: stringCount
#para: aList
#def:  Takes in a list and counts the words in the list and the frequency
#      they appear in the list.
def stringCount(aList):
    dict = {}
    newList = []
    ######Creates Dictionary
    for newkey in aList:
        ##adds to newList if not already in the dictionary
        if newkey not in dict:
            newList.append(newkey)
        ##creates a key or finds a key and increments it by 1
        dict[newkey] = dict.get(newkey,0)+1
    ######
    newList.sort()
    aList.clear()
    ######Creates List
    for x in newList:
        aList.append(x + ' ' + str(dict[x]))
    ######
    for x in aList:
        print(x)
    ######
    return None

#name: isFloat
#para: value
#def:  takes in a value, if its a float the method will return true. else it
#      it will return false if there is a ValueError.
def isFloat(value):
    try:
     float(value)
     return True
    except ValueError:
     return False

#name: class Node
#para: None
#def:  Node class that holds data and next, used for Linked List
class Node:
    #constructor takes in a data type and sets the Node to the data
    def __init__(self,data):
        self.data = data
        self.next = None
    #getData: returns the data in this Node
    def getData(self):
        return self.data
    #setData: takes in newData and sets the Node's data to newData
    def setData(self, newData):
        self.data = newData
    #getNext: returns what is after this node
    def getNext(self):
        return self.next
    #setNext: takes in a new Node that this node will now go before.
    def setNext(self,newNode):
        self.next = newNode

#name: LinkedList
#para: None
#def:  LinkedList uses Node class to create a standard Linked List. Linked List
#      holds size of the list, can delete, search, insert, and print.
class LinkedList:
    #Linked List Constructor creates head.
    def __init__(self):
        self.head=None
    #insert: function creates newNode sets newNode to what head is pointing to
    #and then makes head point to the newNode
    def insert(self,data):
        newNode = Node(data)
        newNode.setNext(self.head)
        self.head = newNode
    #printLL: searches through each node with a tempHead and prints out the data
    def printLL(self):
        tempHead = self.head
        while tempHead != None:
            print(tempHead.getData(), ' ', end="")
            tempHead = tempHead.getNext()
        print('')
    #delete: searches through each node and deletes the node. There are two
    #cases. If its in the front of the list and if it isn't
    def delete(self,data):
        tempHead = self.head
        prev = self.head
        found = False
        while tempHead!=None and found is False:
            if tempHead.getData() == data:
                if self.head == tempHead:
                    self.head = self.head.getNext()
                    found = True
                else:
                    prev.setNext(tempHead.getNext())
                    found = True
            else:
                prev = tempHead
                tempHead = tempHead.getNext()
    #search: goes through the list and tries to find data
    def search(self,data):
        tempHead = self.head
        found = False
        while tempHead!=None and found is False:
            if tempHead.getData() == data:
                found = True
                return True
            else:
                tempHead = tempHead.getNext()
        return False
    #size: loops through the list and counts the nodes, adding to 'size'
    #then returns 'size'
    def size(self):
        tempHead = self.head
        size = 0
        while tempHead is not None:
            size+=1
            tempHead = tempHead.getNext()
        return size
