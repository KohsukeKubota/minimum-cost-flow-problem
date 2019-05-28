import networkx as nx


# 有向グラフ(Directed Graph)
G = nx.DiGraph()

# 頂点の追加
G.add_node('s', color='red', demand=-4)
G.add_node('t', color='red', demand=4)
G.add_node('a')
G.add_node('b')
G.add_node('c')
G.add_node('d')

# 辺の追加
G.add_edge('s', 'a', capacity=2, weight=2)
G.add_edge('s', 'c', capacity=7, weight=4)
G.add_edge('a', 'b', capacity=4, weight=6)
G.add_edge('a', 'c', capacity=2, weight=1)
G.add_edge('c', 'b', capacity=1, weight=6)
G.add_edge('c', 'd', capacity=6, weight=2)
G.add_edge('d', 'b', capacity=3, weight=2)
G.add_edge('b', 't', capacity=7, weight=2)
G.add_edge('d', 't', capacity=2, weight=7)

nx.nx_agraph.view_pygraphviz(G, prog='fdp')
flow_cost, flow_dict = nx.network_simplex(G)
print(flow_cost)
print(flow_dict)
