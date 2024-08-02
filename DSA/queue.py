class node:
    def __init__(self,value):
        self.value = value
        self.next = None
class queue:
    def __init__(self,value):
        new_node = node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
    
    def enqueue(self,value):
        new_node = node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):

        if self.length==0:
            return None
        temp = self.first
        if self.length ==1:
            self.first = None
            self.last = None         
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp

    def print_queue(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next

q = queue(0)
q.enqueue(1)
q.dequeue()
q.print_queue()