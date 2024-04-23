import copy
from queue import PriorityQueue

"""
    name:  Jacob Susko
    Longest Path Exact Solution
    Directions for running:
"""


def main():
    one, two = input().split()
    num_verticies, num_edges = int(one), int(two)
    
    graph = {chr(97 + i): {} for i in range(num_verticies)}
    neg_graph = copy.deepcopy(graph)
    for _ in range(num_edges):
        a, b, c = input().split()
        graph[a][b] = int(c)
        neg_graph[a][b] = int(c) * -1

    dijkstra(neg_graph, num_verticies)
    pass

"""
    Got idea to use dijkstra from: 
    https://stackoverflow.com/questions/8027180/dijkstra-for-longest-path-in-a-dag#:~:text=The%20Dijkstra%20algorithm%20finds%20the,be%20actualy%20the%20longest%20path.
    
    I reference the code I used to complete lab 10
"""
def dijkstra(graph, num_verticies):
    results = []
    paths = []
    for i in range(num_verticies):
        results.append(dijkstra_alg(chr(97+i), graph, num_verticies))
        paths.append(find_path(results[i], chr(97+i)))
        # print(chr(97+i), '\n', results[i], '\n')
    long_path = max(paths, key=lambda x: x[0])
    print(long_path[0])
    for node in long_path[1][:-1]:
        print(node, end=' ')
    print(long_path[1][-1])


def find_path(result, start):
    low = float('inf')
    end = ''
    for node in result:
        if result[node][1] < low:
            low = result[node][1]
            end = node

    path = [end]
    cur = end
    while cur != start:
        cur = result[cur][0]
        path.insert(0, cur)
    return (low*-1, path)


def dijkstra_alg(start, graph, num_verticies):
    init = InitSSSP(start, num_verticies)
    pq = PriorityQueue()  # (shortest distance, vertex)

    pq.put((0, start))
    while not pq.empty():
        (distance, u) = pq.get()
        for v, weight in graph[u].items():
            if init[v][1] > distance + weight:
                init[v][0] = u
                init[v][1] = distance + weight
                pq.put((init[v][1], v))
    return init


def InitSSSP(start, num_verticies):
    res = {}
    res[start] = [None, 0]
    for v in range(num_verticies):
        if (chr(97 + v)) != start:
            res[chr(97 + v)] = [None, float('inf')]
    return res


if __name__ == "__main__":
    main()
