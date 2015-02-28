import sys, math
"""
The Node class
"""
class Node():
    def __init__(self, nb):
        self.nb = nb    #Node id
        self.gateway = False #wthether the node is a gateway
        self.cost = sys.maxint #initialize the cost to infinite for Dijkstra algo
        self.succ = [] #successors : Nodes that we can reach from this node
        self.prev = None #The parent node (for Disjktra algo)

"""
Returns the node having the minimal cost
@param Q the list of nodes
"""
def min_dij(Q):
    min_node=Q.values()[0]
    for node in Q.values():
        if node.cost < min_node.cost:
            min_node = node
    return min_node
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# N: the total number of nodes in the level, including the gateways
# L: the number of links
# E: the number of exit gateways
N, L, E = [int(i) for i in raw_input().split()]

graph = {} #the graph
node1 = None #first node of the link
node2 = None #second node of the link
cutted = None #link is cutted or not
dest = [] #the destination nodes
Q={}
#Construction of the graph
for i in xrange(L):
    # N1: N1 and N2 defines a link between these nodes
    N1, N2 = [int(i) for i in raw_input().split()]
    node1 = Node(N1);
    node2 = Node(N2); 
    if graph: #if the graph is not empty
        if not graph.has_key(N1): #if the graph does not contain the node N1
            graph[N1]=node1
        else:
            node1 = graph[N1]
        if not graph.has_key(N2): #if the graph does not contain the node N2
            graph[N2]=node2
        else:
            node2 = graph[N2]
    else: #retrieve the corresponding nodes
        graph[N1] = node1
        graph[N2] = node2
    
    #Add the links    
    node1.succ.append(node2)
    node2.succ.append(node1)

#Get the gateways    
for i in xrange(E):
    EI = int(raw_input()) # the index of a gateway node
    dest.append(graph[EI])
    for  link in graph :
        graph[EI].gateway = True
        

# game loop
# Idea : Cut the links with are the shortest paths to the destination
# Use Dijkstra algo to find the shortest path
while 1:
    SI = int(raw_input()) # The index of the node on which the Skynet agent is positioned this turn
    #find a link to cut
    index=0
    g = graph.copy()
    g[SI].cost = 0 #The initial cost of the initial node = 0
    #Initialize dijstra algo
    Q = g.copy()
    for n in g.values():
        if n.nb != SI:
            n.cost = sys.maxint
    #Disjktra main loop
    while Q:
        u = min_dij(Q)
        del Q[u.nb]
        
        for v in u.succ:
            alt = u.cost+1
            if alt < v.cost:
                v.cost = alt
                v.prev = u
    
    min_dest = dest[0]
    #case many gateways find the link leading to the nearest gateway
    for d in dest:
        if d.prev.cost < min_dest.prev.cost:
            min_dest = d
    
    #cut this node
    cutted = (min_dest.prev.nb, min_dest.nb)

    print "%s %s"%cutted 
