"""

ELEC 365 - Algorithms I
Nicholas Alderman - Assignment 1
September 18 - Dijkstras Algorithm

"""




class graph:
    def __init__(self, maxVertex):
        self.maxVertex = maxVertex
        self.vertexs = {}
        self.head = None
    def setHead(self, node):
        self.head = node
    def addNode(self, node):
        self.vertexs[node.name] = node
        
        
class node:
    def __init__(self, name):
        self.name = name
        self.neighbours = []
    def addNeighbour(self, node, weight):
        self.neighbours.append({"node": node, "weight": weight})
        
class dijkstras:
    def __init__(self, graph):
        self.Cost = {}
        self.Reached = {}
        self.Estimate = {}
        self.Candidate = {}
        self.Predecessor = {}
        self.graph = graph
        
        for vertex in self.graph.vertexs:
            self.Reached[vertex] = False
            self.Cost[vertex] = float('inf')
            self.Estimate[vertex] = float('inf')
            self.Predecessor[vertex] = None
            self.Candidate[vertex] = False
            
        
    def algorithm(self):
        self.Cost[self.graph.head.name] = 0
        self.Reached[self.graph.head.name] = True
        
        for neighbour in self.graph.head.neighbours:
            self.Estimate[neighbour['node'].name] = neighbour['weight']
            self.Candidate[neighbour['node'].name] = True
            
        for __ in self.graph.vertexs:
            bce = float('inf')
            for vert in self.graph.vertexs:
                if self.Candidate[vert] == True and self.Estimate[vert] < bce:
                    v = vert
                    bce = self.Estimate[vert]
            self.Cost[v] = self.Estimate[v]
            self.Reached[v] = True
            self.Candidate[v] = False
            
            for vertNeighbour in self.graph.vertexs[v].neighbours:
                if (vertNeighbour['weight'] > 0) and (self.Reached[vertNeighbour['node'].name] == False):
                    if self.Cost[v] + vertNeighbour['weight'] < self.Estimate[vertNeighbour['node'].name]:
                        self.Estimate[vertNeighbour['node'].name] = self.Cost[v] + vertNeighbour['weight']
                        self.Candidate[vertNeighbour['node'].name] = True
                        self.Predecessor[vertNeighbour['node'].name] = v
        return self.Cost
       
exFiles = ["Dijkstra_Data_6.txt","Dijkstra_Data_100.txt","Dijkstra_Data_200.txt","Dijkstra_Data_400.txt","Dijkstra_Data_800.txt","Dijkstra_Data_1600.txt"]        
    
for openFile in exFiles:

    with open(openFile) as f:
        s = f.read()
        s = s.strip()
        s = s.splitlines()
        
    testGraph = graph(int(s.pop(0)))
    for i in range(testGraph.maxVertex):
        if i == 0:
            head = node(i)
            testGraph.setHead(head)
            testGraph.addNode(head)
        else:
            testGraph.addNode(node(i))
        
    for fromVertex, val in enumerate(s):
        val = val.split()
        for toVertex, weight in enumerate(val):
            if weight != '0':
                #print ("from " + str(fromVertex) + " To " + str(toVertex) + " Weight " + weight)
                testGraph.vertexs[fromVertex].addNeighbour(testGraph.vertexs[toVertex],int(weight))
        
        
    dijk = dijkstras(testGraph)
    result = dijk.algorithm()
    
    tmp = 0
    tmp2 = 0
    for i in result:
        if tmp < result[i]:
            tmp = result[i]
            tmp2 = i 
            
    print ("    File: " +openFile + " Vertex: " + str(tmp2) + " Cost: " + str(tmp))