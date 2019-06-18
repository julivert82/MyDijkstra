class graph:

    def __init__(self):
        self.g = {}

    def addvertex(self, v):
        self.g.update({v.name:v.neighbors})

    def printgraph(self):
        print(self.g)

    def partialDijkstra(self, p, s, b, currentcost):
        pathcost = 0
        edges = self.g[p]
        if b.name in dict(edges).keys(): #direct path
            print('Direct path found at {0} by {1}'.format(p, str(dict(edges)[b.name] + currentcost)))
            return (dict(edges)[b.name] + currentcost)
        else: #there is no direct path
            for edge in edges:
                if s != edge[0]:
                    print('Calculating cost via {0} with {1}'.format(edge[0], str(currentcost+edge[1])))
                    cost = self.partialDijkstra(edge[0], p, b, currentcost+edge[1])
                    if pathcost == 0:
                        pathcost = cost
                    else:
                        if pathcost > cost:
                            pathcost = cost
            return pathcost

    def dijkstraAB(self, a, b):
        if a.name not in self.g.keys() or b.name not in self.g.keys():
            return -1
        else:
            pathcost = 0
            edges = self.g[a.name]
            if b.name in dict(edges).keys(): #direct path
                print('Direct path found at {0}'.format(a.name))
                return dict(edges)[b.name]
            else: #there is no direct path
                for edge in edges:
                    print('Calculating cost via {0} with {1}'.format(edge[0], str(edge[1])))
                    cost = self.partialDijkstra(edge[0], a.name, b, edge[1])
                    if pathcost == 0:
                        pathcost = cost
                    else:
                        if pathcost > cost:
                            pathcost = cost
                return pathcost


class vertex:

    def __init__(self, n):
        self.neighbors = []
        self.name = n

    def addneighbor(self, n, cost):
        self.neighbors.append((n.name, cost))


if __name__ == '__main__':
    # Testing graph 1
    '''
    A ----100-----B
    |             |
    50           80
    |             |
    C-----140-----D
    '''
    print("Testing graph 1")
    g1 = graph()
    v1 = vertex('a')
    g1.addvertex(v1)
    v2 = vertex('b')
    v1.addneighbor(v2, 100)
    g1.addvertex(v2)
    v3 = vertex('c')
    v1.addneighbor(v3, 50)
    g1.addvertex(v3)
    v4 = vertex('d')
    v3.addneighbor(v4, 140)
    g1.addvertex(v4)
    v2.addneighbor(v4, 80)
    g1.printgraph()
    #v5 = vertex('e')
    e = g1.dijkstraAB(v1,v4)
    if e == -1:
        print('One of the vertex doesn\'t belong to this graph')
    else:
        print('Cost of direct path is {0}'.format(e))
    # Testing graph 2
    '''
    A-----100-----B-----50-----E
    |             |            |
    50           80           25
    |             |            |
    C-----140-----D-----30-----F
    '''
    print("Testing graph 2")
    g1 = graph()
    v1 = vertex('a')
    v2 = vertex('b')
    v3 = vertex('c')
    v4 = vertex('d')
    v5 = vertex('e')
    v6 = vertex('f')
    v1.addneighbor(v2, 100)
    v1.addneighbor(v3, 50)
    v2.addneighbor(v1, 100)
    v2.addneighbor(v4, 80)
    v2.addneighbor(v5, 50)
    v3.addneighbor(v1, 50)
    v3.addneighbor(v4, 140)
    v4.addneighbor(v2, 80)
    v4.addneighbor(v3, 140)
    v4.addneighbor(v6, 30)
    v5.addneighbor(v2, 50)
    v5.addneighbor(v6, 25)
    v6.addneighbor(v4, 30)
    v6.addneighbor(v5, 25)
    g1.addvertex(v1)
    g1.addvertex(v2)
    g1.addvertex(v3)
    g1.addvertex(v4)
    g1.addvertex(v5)
    g1.addvertex(v6)
    g1.printgraph()
    e = g1.dijkstraAB(v1, v5)
    if e == -1:
        print('One of the vertex doesn\'t belong to this graph')
    else:
        print('Cost of direct path is {0}'.format(e))

    # Testing graph 3
    '''
    A-----100-----B-----50-----E
    |             |            |
    10           80           25
    |             |            |
    C------10-----D-----30-----F
    '''
    print("Testing graph 3")
    g1 = graph()
    v1 = vertex('a')
    v2 = vertex('b')
    v3 = vertex('c')
    v4 = vertex('d')
    v5 = vertex('e')
    v6 = vertex('f')
    v1.addneighbor(v2, 110)
    v1.addneighbor(v3, 10)
    v2.addneighbor(v1, 100)
    v2.addneighbor(v4, 80)
    v2.addneighbor(v5, 50)
    v3.addneighbor(v1, 50)
    v3.addneighbor(v4, 10)
    v4.addneighbor(v2, 80)
    v4.addneighbor(v3, 140)
    v4.addneighbor(v6, 30)
    v5.addneighbor(v2, 50)
    v5.addneighbor(v6, 25)
    v6.addneighbor(v4, 30)
    v6.addneighbor(v5, 25)
    g1.addvertex(v1)
    g1.addvertex(v2)
    g1.addvertex(v3)
    g1.addvertex(v4)
    g1.addvertex(v5)
    g1.addvertex(v6)
    g1.printgraph()
    e = g1.dijkstraAB(v1, v5)
    if e == -1:
        print('One of the vertex doesn\'t belong to this graph')
    else:
        print('Cost of direct path is {0}'.format(e))