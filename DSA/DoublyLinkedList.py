class node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
class Doublylinkedlist:


    def __init__(self,value):
        new_node = node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


    def append(self,value):
        new_node = node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True


    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 0:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp

    def prepend(self,value):
        new_node = node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        temp = self.head
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if index <0 and index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for i in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for i in range(self.length -1 , index , -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0 :
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = node(value)
        before = self.get(index-1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node
        self.length += 1
        return True
    

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value )
            temp = temp.next

    def remove (self,index):
        if index < 0 or index > self.length:
            return False
        if index == 0 :
            return self.pop_first(index)
        if index == self.length:
            return self.pop(index)
        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        # before =   temp.prev
        # after=   temp.next 
        # before.next = after
        # after.prev = before
        temp.next = None
        temp.prev = None
        self.length -=  1
        return temp


DD = Doublylinkedlist(5)
DD.append(6)
DD.append(7)
DD.append(8)
DD.remove(2)
# DD.pop()
# DD.prepend(10)
# DD.set_value(1,9)
# print(DD.get(1))
# DD.pop_first()
# DD.set_value(1,5)
# DD.insert(1,5)
DD.print_list()
