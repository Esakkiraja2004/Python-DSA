class node:
    def __init__(self,value):
        self.value = value
        self.next = None
class linked_list:
    #function for get input
    def __init__(self,value):
        new_node = node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    #function for append the item
    def append(self,value):
        new_node = node(value)
        if self.head ==0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    #function for pop item
    def pop(self):
        if self.head == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length-=1
        if self.length == 0:
            self.head = None
            self.tali =  None
        return temp

    #function for pop_first

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    #function for prepend

    def prepend(self,value):

        new_node = node(value)

        if self.length == 0:

            self.head = new_node
            self.tail = new_node

        else:
            new_node.next = self.head

            self.head = new_node
        self.length += 1

    #function for get by index

    def get(self,index):
        if index <0 or index >= self.length:
            return None
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp

    #function for set_value

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    #function for insert

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0 :
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = node(value)
        temp = self.get(index -1)
        new_node.next = temp.next        
        temp.next = new_node
        self.length += 1
        return True

    # function  fro remove

    def remove(self,index):
        if index < 0 or index > self.length:
            return False
        if index == 0 :
            return self.pop_first(value)
        if index == self.length:
            return self.pop(value)
        pre = self.get(index -1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length+=1
        return temp

    #function for reverse

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for i in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    #functiion print the list
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next




mylist = linked_list(5)
mylist.append(6)
mylist.append(8)
mylist.append(9)
mylist.insert(2,6)
# # mylist.pop()
# # mylist.prepend(10)
# # mylist.prepend(10)
# # mylist.pop_first()
# # mylist.set_value(1,5)
# # mylist.insert(2,12)
# mylist.remove(1)
# mylist.reverse()
print("Element in  Linked List :")
mylist.print_list()
# mylist.set_value(1,12)
# print(mylist.get(3))


