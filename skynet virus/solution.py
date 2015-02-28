import sys, math

class Node():
    def __init__(self, nb):
        self.nb = nb
        self.gateway = False
        self.cost = sys.maxint
        self.succ = []
        self.prev = None
    #def __unicode__(self):
        #return "Node(id=%s, gateway=%s)"%self.id,self.gateway
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

graph = {}
node1 = None
node2 = None
cutted=None
dest = []
Q={}
for i in xrange(L):
    # N1: N1 and N2 defines a link between these nodes
    N1, N2 = [int(i) for i in raw_input().split()]
    node1 = Node(N1);
    node2 = Node(N2); 
    if graph:
        if not graph.has_key(N1):
            graph[N1]=node1
        else:
            node1 = graph[N1]
        if not graph.has_key(N2):
            graph[N2]=node2
        else:
            node2 = graph[N2]
    else:
        graph[N1] = node1
        graph[N2] = node2
        
    node1.succ.append(node2)
    node2.succ.append(node1)
    
for i in xrange(E):
    EI = int(raw_input()) # the index of a gateway node
    dest.append(graph[EI])
    for  link in graph :
        graph[EI].gateway = True
        

# game loop

while 1:
    SI = int(raw_input()) # The index of the node on which the Skynet agent is positioned this turn
    #choose a link to cut
    index=0
    g = graph.copy()
    g[SI].cost = 0
    #dijstra --> shortest path
    Q = g.copy()
    for n in g.values():
        if n.nb != SI:
            n.cost = sys.maxint
    while Q:
        u = min_dij(Q)
        del Q[u.nb]
        
        for v in u.succ:
            alt = u.cost+1
            if alt < v.cost:
                v.cost = alt
                v.prev = u
    min_dest = dest[0]
    for d in dest:
        if d.prev.cost < min_dest.prev.cost:
            min_dest = d
    
    cutted = (min_dest.prev.nb, min_dest.nb)
    print >> sys.stderr, "to cut = ", cutted
    #min_dest.succ.remove(min_dest.prev)
    #min_dest.prev.succ.remove(min_dest)

    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    print >> sys.stderr, cutted
    print "%s %s"%cutted # Example: 0 1 are the indices of the nodes you wish to sever the link between
