class node:
    def __init__(self,value):
        self.value = value
        self.next = None

class stack:

    def __init__(self,value):
        new_node = node(value)
        self.top = new_node
        self.height = 1

    def push(self,value):
        new_node= node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
            self.height += 1

    def pop (self):
        if self.height == 0:
            return None
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            self.height -= 1
            return temp

    def print_stack(self):
        temp =self.top
        while temp:
            print(temp.value)
            temp = temp.next
my_stack= stack(0)
my_stack.push(1)
my_stack.pop()
my_stack.print_stack() 