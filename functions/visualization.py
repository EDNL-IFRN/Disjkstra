import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(graph, shortest_path=None):
    G = nx.Graph()
    
    for v1 in graph.vertices:
        i1 = graph.vertex_index[v1]
        current = graph.array[i1].head
        while current:
            G.add_edge(v1, current.value, weight=current.weight)
            current = current.next

    pos = nx.spring_layout(G, seed=42)
    
    # Draw the graph
    plt.figure(figsize=(12, 8))
    
    nx.draw_networkx_edges(G, pos)
    
    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', 
                          node_size=500)
    
    nx.draw_networkx_labels(G, pos)
    
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels)
    
    if shortest_path:
        path_edges = list(zip(shortest_path[:-1], shortest_path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, 
                             edge_color='r', width=2)

    plt.title("Graph Visualization")
    plt.axis('off')
    plt.show()
