import networkx as nx
import matplotlib.pyplot as plt


def Dijkstra():
    G = nx.Graph()
    G.add_nodes_from(range(1, 28))
    Node = nx.nodes(G)
    edge=[('Вінниця', 'Житомир', 127),('Вінниця','Київ',227),
               ('Вінниця', 'Кіровоград',320),
                   ('Вінниця','Миколаїв',428),
                   ('Вінниця','Odessa',423),
                   ('Вінниця','Cherkassy',341),
                   ('Вінниця','Chernivtsy',276),
          ('Київ', 'Львів', 500)]
    print(edge)
    G.add_weighted_edges_from(edge)
    visited = []
    path = []
    first_node = []
    while Node:
        first_node.append(0)
        visited.append(first_node)

    print(Node)








Dijkstra()



    
