import sys
from model.graph import Graph

def dijkstra(graph: Graph, start_vertex: str):
    D = {v: sys.maxsize for v in graph.vertices}
    D[start_vertex] = 0

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
            current_node = current_node.next

    return D
