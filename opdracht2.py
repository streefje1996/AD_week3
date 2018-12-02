class ListNode:
    def __init__(self,data,next_node):
        self.data = data
        self.next = next_node

    def __repr__(self):
        return str(self.data)

class MyCircularLinkedList:
    def __init__(self):
        self.tail = None

    def __repr__(self):
        s = ''
        last = self.tail        
        if last != None:
            current = last.next
            s = s + str(current)
            if current == last:
                return s
            current = current.next
            while current != last:
                s = s + " -> " + str(current)
                current = current.next
            s = s + " -> " + str(last)
        if not s: # s == '':
            s = 'empty list'
        return s

    def addLast(self,e):
        if not self.tail: # self.head == None:
            self.tail = ListNode(e,None)
            self.tail.next = self.tail
        else:
            n = ListNode(e,self.tail.next)
            self.tail.next = n
            self.tail = n

    def delete(self,e):
        if self.tail: # self.head != None:
            if self.tail.next == self.tail:
                if self.tail.data == e:
                    self.tail = None

            else:
                last = self.tail
                current = last.next
                while current != last:
                    if current.data == e:
                        n = current.next
                        while n != current:
                            prev = n
                            n = n.next
                        prev.next = current.next
                        current.tail = None
                    current = current.next
        #print("List is empty you fool")

mylist =  MyCircularLinkedList()
print(mylist)
mylist.addLast(1)
mylist.addLast(2)
mylist.addLast(3)
print(mylist)
mylist.delete(2)
print(mylist)
mylist.delete(1)
mylist.addLast("Frits is da bomb")
print(mylist)
mylist.delete(3)
print(mylist)

