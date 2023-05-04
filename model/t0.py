import numpy as np


class node:
    def __init__(self):
        self.degree = 0
        self.conn_nodes = []
        self.view_id = 'V_0'
        self.node_data = null
    
    def connNode(self, n2: node, e=null):
        if n2 in conn_nodes: return

        if e == null: e = edge(self, n2)

        self.conn_nodes.append([n1,e])
        self.degree += 1

        n2.connNode_E(self,e)

        

class edge:
    def __init__(self):
        self.conn_nodes = []
        self.multiplicity = 0
        self.edge_data = null
        self.view_id = 0
    
    def __init__(self, n1:node, n2:node):
        self.conn_nodes = [n1, n2]
        self.multiplicity = 2
        self.edge_data = ""

        self.view_id = n1.view_id + n2.view_id + '_E'

class graph:
    def __init__(self):
        self.head = null
        self.nV = 0
        self.nE = 0
        
        self.search_metrics = []
        self.search_nodes = {}

        self.view_id = 'G_0'
    
    def initMinimalGraph(self):
        self.head = node()
        self.nV = 1
    
    def initByHead(self, h:node):
        self.head = h
        



class forest:
    def __init__(self):
        self.heads = []



##############################################
#   ingestion and display
##############################################

def createNew():
    f = forest()
    g = graph().initMinimalGraph()
    f.heads.append(g)

    return f, f.heads[0]

def feedAdjMat(adj_mat:[[]]):
    nV = adj_mat.length()
    nlist = [ node() for i in range(nV) ]

    for i in range(nV):
        for j in range(nV):
            if adj_mat[i][j]:
                nlist[i].connNode(nlist[j])

    h, nVs = findHeads(adj_mat)
    h = [ _[1] for _ in sorted(zip(nVs, h)) ]

    h = [ findCentroid(adj_mat, hi[1]) for hi in h ]

    #create the forest
    f = forest()
    f.heads = [ graph().initByHead(nlist[i]) for i in h ]

    return f, f.heads[0]






