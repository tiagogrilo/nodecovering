import networkx as nx
import matplotlib.pyplot as plt

# creating graph
G = nx.Graph()

# adding nodes: [1,10[
G.add_nodes_from(list(range(1,10)))

# adding edges
G.add_edges_from([(1, 6), (1, 8), (2,3), (2,5), (2,7), (3,4), (3,6), (4,5), (4,9), (5,8), (6,7), (6,9), (7,8), (8,9)])

#create copy of G
J = nx.Graph()
J.add_nodes_from(list(range(1,10)))
J.add_edges_from([(1, 6), (1, 8), (2,3), (2,5), (2,7), (3,4), (3,6), (4,5), (4,9), (5,8), (6,7), (6,9), (7,8), (8,9)])

print("Graph contains", G.number_of_nodes(), "nodes and", G.number_of_edges(), "edges.")

# drawing the graph and saving to "path.png" in the local directory, it may take a few iterations to create a nice looking graph
plt.figure(1)
nx.draw(G, with_labels=True, font_weight='bold')
plt.savefig("path.png")

# function to determine the node with most edges. if it's a tie, it chooses the first.
def biggest_node():
	big_node = -1
	for edges_node in G.nodes():
		if len(G.edges([edges_node])) > big_node:
			big_node = edges_node
	return big_node

H = nx.Graph()

def heuristic():
	# main heuristic
	while G.number_of_nodes() > 0:
		big_node = biggest_node()
		H.add_node(big_node)
		H.add_nodes_from(list(G.neighbors(big_node)))
		H.add_edges_from(list(G.edges(big_node)))
		node_list = list(G.neighbors(big_node))
		G.remove_nodes_from(list(G.neighbors(big_node)))
		G.remove_node(big_node)
		for edges_node in G.nodes():
			for node in node_list:
				if J.has_edge(edges_node, node):
					H.add_edge(edges_node,node)
					J.clear()
					break

heuristic()
# edge connectivity is the minimum number of edges, lambda(G), whose deletion from a graph G disconnects G, also called the line connectivity
# the edge connectivity of a disconnected graph is 0, while that of a connected graph with a graph bridge is 1.
print("Edge connectivity is", nx.edge_connectivity(H),"edge(s).")
print("Graph contains", H.number_of_nodes(), "node(s) and", H.number_of_edges(), "edge(s).")
# drawing the graph and saving to "path1.png" in the local directory, it may take a few iterations to create a nice looking graph
plt.figure(2)
nx.draw(H, with_labels=True, font_weight='bold')
plt.savefig("path1.png")



