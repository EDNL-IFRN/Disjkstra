import csv
from model.graph import Graph
from functions.disjkstra import dijkstra

def add_edges(file_path, graph: Graph):
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader, None)
        for row in csv_reader:
            graph.add_edge(row[0], row[1], int(row[2]))

def get_vertices(file_path):
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader, None)
        vertices = set()
        for row in csv_reader:
            vertices.add(row[0])
            vertices.add(row[1])
    return list(vertices)

def main():
    file_path = 'docs/edges.csv'
    vertices = get_vertices(file_path)
    graph = Graph(vertices)
    add_edges(file_path, graph)
    graph.print_graph()

    start_vertex = input("Digite o vértice inicial: ")
    end_vertex = input("Digite o vértice final: ")

    distances = dijkstra(graph, start_vertex)
    print(f"A menor distância de {start_vertex} para {end_vertex} é {distances[end_vertex]}")

if __name__ == '__main__':
    main()