import networkx as nx
import random


G = nx.Graph()

numberofNodes = 10
probOfDistr = 0.5
probOfAccept = 0.5
numberOfExp = 100


CounterofOne = 0
CounterofZero = 0


class GerenateGraph:

    def __init__(self, probOfDistr):
        self.probOfDistr = probOfDistr
        self.counterofOne = 0
        self.counterofZero = 0
        self.G = nx.Graph()

    def decision(self, probOfDistr):
        return random.random() < probOfDistr

    def allToAllGraph(self, numberofNodes, probOfDistr):
        CounterofOne = self.counterofOne
        CounterofZero = self.counterofZero
        G = self.G

        for i in range(0, numberofNodes):
            G.add_node(i, opinion=self.decision(probOfDistr))
            if G.node[i]['opinion'] == 1:
                CounterofOne = CounterofOne + 1
            else:
                CounterofZero = CounterofZero + 1
        for i in range(0, numberofNodes):
            for j in range(0, numberofNodes):
                if i != j:
                    G.add_edge(j, i)

        print('CounterofOne=', CounterofOne)
        print('CounterofZero=', CounterofZero)
        return [G, CounterofOne, CounterofZero]

    def ringGraph(self, numberofNodes, probOfDistr):
        CounterofOne = self.counterofOne
        CounterofZero = self.counterofZero
        G = self.G

        for i in range(0, numberofNodes):
            G.add_node(i, opinion=self.decision(probOfDistr))
            if G.node[i]['opinion'] == 1:
                CounterofOne = CounterofOne + 1
            else:
                CounterofZero = CounterofZero + 1

        for i in range(0, numberofNodes):
            G.add_edge(i, i + 1)
        G.add_edge(numberofNodes, 1)
        print('CounterofOne=', CounterofOne)
        print('CounterofZero=', CounterofZero)
        return [G, CounterofOne, CounterofZero]


class Programm:
    def __init__(self):
        pass

    def program(self, numberofNodes, probOfDistr, graphType):

        gerenateGraph = GerenateGraph(probOfDistr)
        if graphType:
            graph = gerenateGraph.allToAllGraph(numberofNodes, probOfDistr)
        else:
            graph = gerenateGraph.ringGraph(numberofNodes, probOfDistr)

        CounterofIteration = 0

        G = graph[0]
        CounterofOne = graph[1]
        CounterofZero = graph[2]

        if (CounterofOne != 0) and (CounterofZero != 0):

            while (CounterofOne != 0) or (CounterofZero != 0):

                for i in range(0, numberofNodes):
                    a = random.randint(0, numberofNodes - 1)
                    b = random.choice(list(G.neighbors(a)))

                    nodeA = G.nodes[a].get('opinion')
                    nodeB = G.nodes[b].get('opinion')

                    CounterofIteration = CounterofIteration + 1

                    if nodeA != nodeB:
                        if gerenateGraph.decision(probOfAccept):
                            G.nodes[b]['opinion'] = nodeA

                            if G.nodes[b].get('opinion'):
                                CounterofOne = CounterofOne + 1
                                CounterofZero = CounterofZero - 1
                            else:
                                CounterofOne = CounterofOne - 1
                                CounterofZero = CounterofZero + 1

                        if (CounterofOne == 0) or (CounterofZero == 0):
                            break

                if (CounterofOne == 0) or (CounterofZero == 0):
                    break

        print('CounterofIteration=', CounterofIteration)
        print('CounterofOne=', CounterofOne)
        print('CounterofZero=', CounterofZero)
        return CounterofIteration

    def rez(self, numberofNodes, numberOfExp, graphType, probOfDistr):

        iterations = 0
        for i in range(0, numberOfExp):
            prog = self.program(numberofNodes, probOfDistr, graphType)
            iterations += prog
        print(iterations // numberOfExp)
        return True

pr = Programm()
pr.rez(numberofNodes, numberOfExp, 1, probOfDistr)

# 1- all-to-all
# 0- ring

# print(G.nodes[1])
# print(G.nodes[3])
#
# print('колличество узлов:', G.number_of_nodes())  # колличество узлов
# print('колличество ребер:', G.number_of_edges())  # колличество ребер
# print('список узлов:', list(G.nodes))  # список узлов
# print('список ребер:', list(G.edges))  # список ребер
# print('список соседей узла 1:', list(G.adj[1]))  # список соседей узла 1
# print('список соседей узла 1', list(G.neighbors(1)))  # список соседей узла 1
# print('степень вершины 1:', G.degree[1])  # the number of edges incident to 1
#
# def decision(probOfDistr):
#     return random.random() < probOfDistr
#
#
# def ringMatrix(numberofNodes, probOfDistr):
#     CounterofOne = 0
#     CounterofZero = 0
#
#     for i in range(0, numberofNodes):
#         G.add_node(i, opinion = decision(probOfDistr))
#         if G.node[i]['opinion'] == 1:
#             CounterofOne = CounterofOne + 1
#         else:
#             CounterofZero = CounterofZero + 1
#
#     for i in range(0, numberofNodes):
#         G.add_edge(i, i + 1)
#     G.add_edge(numberofNodes, 1)
#     print('CounterofOne=', CounterofOne)
#     print('CounterofZero=', CounterofZero)
#     return [G, CounterofOne, CounterofZero]
#
#
# def allToAllMatrix(numberofNodes, probOfDistr):
#     CounterofOne = 0
#     CounterofZero = 0
#
#     for i in range(0, numberofNodes):
#         G.add_node(i, opinion=decision(probOfDistr))
#         if G.node[i]['opinion'] == 1:
#             CounterofOne = CounterofOne + 1
#         else:
#             CounterofZero = CounterofZero + 1
#     for i in range(0, numberofNodes):
#         for j in range(0, numberofNodes):
#             if i != j:
#                 G.add_edge(j, i)
#
#     print('CounterofOne=', CounterofOne)
#     print('CounterofZero=', CounterofZero)
#     return [G, CounterofOne, CounterofZero]
#
#
# def program(numberofNodes, probOfDistr, matrixType):
#
#     if matrixType:
#         matrix = allToAllMatrix(numberofNodes, probOfDistr)
#     else:
#         matrix = ringMatrix(numberofNodes, probOfDistr)
#
#     CounterofIteration = 0
#
#     CounterofOne = matrix[1]
#     CounterofZero = matrix[2]
#
#     if (CounterofOne != 0) and (CounterofZero != 0):
#
#         while (CounterofOne != 0) or (CounterofZero != 0):
#
#             for i in range(0, numberofNodes):
#                 a = random.randint(0, numberofNodes - 1)
#                 b = random.choice(list(G.neighbors(a)))
#
#                 nodeA = G.nodes[a].get('opinion')
#                 nodeB = G.nodes[b].get('opinion')
#
#                 CounterofIteration = CounterofIteration + 1
#
#                 if nodeA != nodeB:
#                     if decision(probOfAccept):
#                         G.nodes[b]['opinion'] = nodeA
#
#                         if G.nodes[b].get('opinion'):
#                             CounterofOne = CounterofOne + 1
#                             CounterofZero = CounterofZero - 1
#                         else:
#                             CounterofOne = CounterofOne - 1
#                             CounterofZero = CounterofZero + 1
#
#                     if (CounterofOne == 0) or (CounterofZero == 0):
#                         break
#
#             if (CounterofOne == 0) or (CounterofZero == 0):
#                 break
#
#
#     print('CounterofIteration=', CounterofIteration)
#     print('CounterofOne=', CounterofOne)
#     print('CounterofZero=', CounterofZero)
#     return CounterofIteration
#
# def rez(numberOfExp , typeMatrix = 1):
#
#     iterations = 0
#
#     for i in range(0, numberOfExp):
#         prog = program(numberofNodes, probOfDistr, typeMatrix)
#         iterations += prog
#
#     print(iterations//numberOfExp)
#
# rez(numberOfExp, 0)

# print(G.nodes[1])
# print(G.nodes[3])
#
# print('колличество узлов:', G.number_of_nodes())  # колличество узлов
# print('колличество ребер:', G.number_of_edges())  # колличество ребер
# print('список узлов:', list(G.nodes))  # список узлов
# print('список ребер:', list(G.edges))  # список ребер
# print('список соседей узла 1:', list(G.adj[1]))  # список соседей узла 1
# print('список соседей узла 1', list(G.neighbors(1)))  # список соседей узла 1
# print('степень вершины 1:', G.degree[1])  # the number of edges incident to 1