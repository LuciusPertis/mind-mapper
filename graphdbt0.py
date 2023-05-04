#graph-collection-test0

import time

class Think_node:
    '''base class for a bubble or box whatever, which requires connection btw each other.
    '''

    def __init__(self, globalidx=None) -> None:
        self.globalidx = globalidx
        self.marker = time.time_ns()

        self.connections = []
        self.basetext = 'empty'
        self.baseattr = [] #Todo attr set for graph manipulation and some instance data
        pass

    def addConnect(self, node, ctype):
        pass

    def remConnect(self, node):
        pass

    def getNode(self):
        return self.globalidx, self


    

if __name__ == '__main__':
    import cv2 as cv
    import numpy as np

    #make a 2D canvas
    canvas = Canvas((1080,1080))

    # - click on cv image to get focus on node
    # - use cli to perform node func like 
    # -- add to node
    # -- change existing or add new connection
    # -- change connection type
    # -- change node data

    startnode = Think_node(0)

    canvas.mapobj(startnode, loc=[0,0])

    focus = startnode


    




    pass