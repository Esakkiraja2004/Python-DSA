class graph:
    def __init__(self):
        self.adj_list = {}
    def add_vet(self,vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    def add_edge(self,v1,v2):
        if v1 in  self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    def rem_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
                return True
            except ValueError:
                pass
        return False
    def rem_vet(self,vertex):
        if vertex in self.adj_list.keys():
            for other_vet in self.adj_list[vertex]:
                self.adj_list[other_vet].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False
    def p_g(self):
        for vertex in self.adj_list:
            print(vertex,":",self.adj_list[vertex])

g = graph()
g.add_vet("A")
g.add_vet("B")
g.add_vet("C")
g.add_vet("D")
g.add_edge("A", "B")
g.add_edge("B","C")
g.add_edge("C","A")
g.add_edge("A", "D")
g.rem_edge("A", "D")
g.rem_vet("D")
g.p_g()