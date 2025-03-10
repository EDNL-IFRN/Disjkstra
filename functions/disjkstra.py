import sys
from model.graph import Graph

def dijkstra(graph: Graph, start_vertex: str, end_vertex: str):
    D = {v: sys.maxsize for v in graph.vertices}
    D[start_vertex] = 0
    
    predecessor = {v: None for v in graph.vertices}
    
    unvisited_vertices = set(graph.vertices)

    while unvisited_vertices:
        min_vertex = None
        for vertex in unvisited_vertices:
            if min_vertex is None:
                min_vertex = vertex
            elif D[vertex] < D[min_vertex]:
                min_vertex = vertex

        if D[min_vertex] == sys.maxsize:
            break

        unvisited_vertices.remove(min_vertex)
        current_node = graph.array[graph.vertex_index[min_vertex]].head

        while current_node:
            distance = D[min_vertex] + (current_node.weight if current_node.weight else 1)
            if distance < D[current_node.value]:
                D[current_node.value] = distance
                predecessor[current_node.value] = min_vertex
            current_node = current_node.next

    path = []
    current = end_vertex
    while current is not None:
        path.append(current)
        current = predecessor[current]
    path.reverse()

    return D, path
