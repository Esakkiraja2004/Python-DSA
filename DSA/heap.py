class mheap:

    def __init__(self):
        self.heap = []

    def left_child(self,index):
        return  2*(index + 1)

    def right_child(self,index):
        return 2*(index + 2)

    def get_parent(self,index):
        return(index -1)//2

    def _swap(self,ind_1,ind_2):
        self.heap[ind_1] ,self.heap[ind_2] = self.heap[ind_2],self.heap[ind_1]

    def _insert(self,value):
        self.heap.append(value)
        current = len(self.heap)-1
        while current > 0 and self.heap[current] > self.heap[self.get_parent(current)]:
            self._swap(current,self.get_parent(current))
            current = self.get_parent(current)

    def sink_down(self, index):
        max_index = index
        left = self.left_child(index)
        right = self.right_child(index)
        while True:
            if left < len(self.heap) and self.heap[left] > self.heap[max_index]:
                max_index = left
            if right < len(self.heap) and self.heap[right] > self.heap[max_index]:
                max_index = right
            if max_index != index:
                self._swap(index, max_index)
                index = max_index
                left = self.left_child(index)  
                right = self.right_child(index)  
            else:
                return 


    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap)  == 1:
            return self.heap.pop()
        max_heap = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.sink_down(0)
        return max_heap
        
mh = mheap()
mh._insert(10)
mh._insert(25)
mh._insert(30)
mh._insert(17)
mh._insert(15)
mh._insert(100)
mh.remove()
print(mh.heap)