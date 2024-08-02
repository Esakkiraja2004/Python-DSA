class hashtable:
    def __init__(self,size=10):
        self.data_map = [None] *10

    def _hash(self,key):

        my_hash = 0
        for letter in   key:
            # my_hash  = (my_hash + ord(letter)*23) % len(self.data_map)
            my_hash = ord(letter)%10
        return my_hash

    def set_value(self, key,value):

        index = self._hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key,value])

    def get_value(self, key):
        index = self._hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])) :
                if self.data_map[index][i][0] == key :
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        all_keys = []

        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys

    def print_hash(self):
        for i , val in enumerate(self.data_map):
            print(i ,":", val)

ht = hashtable()
ht.set_value("ram kumar",25)
ht.set_value("raja",18)
ht.set_value("raja",1)
# print("The value is:" , ht.get_value("raja"))
# print(ht.keys())
ht.print_hash()