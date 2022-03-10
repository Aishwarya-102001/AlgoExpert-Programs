
#** RECURSIVE METHOD ***********
#** Time = O(v + e) --> where v = no.of vertices & e = no. of edges 
#**                     i.as we are traversing every vertex of graph which gives O(v) 
#**                     ii.as we call DFS func at every child node, we use edges to traverse which gives O(e)     
                                                          
#** Space = O(v) --> i. as we store an array of "v" different vertices/nodes
#**                  Ii. as we keep adding frames of call stacks for every function call

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array
