import queue, copy

"""
    name:  Jacob Susko
    Longest Path Exact Solution
    Directions for running:
"""


def main():
    one, two = input().split()
    num_verticies, num_edges = int(one), int(two)
    
    graph = {i: {} for i in range(num_verticies)}

    for _ in range(num_edges):
        a, b, c = input().split()
        graph[int(a)][int(b)] = int(c)

    path, weight = findLongest(graph)
    print(weight)
    for p in path[:-1]:
        print(p, end=' ')
    print(path[-1])


def findLongest(graph):
    longest_path = None
    max_weight = 0
    for start in graph:
        for end in graph:
            paths = dfs(graph, end, start)
            for path, weight in paths:
                if weight > max_weight:
                    longest_path = path
                    max_weight = weight
    return longest_path, max_weight


def dfs(graph, end, start):
    paths = []
    visited = set()
    recurDFS(graph, start, end, [start], 0, visited, paths)
    return paths


def recurDFS(graph, current, end, path, weight, visited, paths):
    if current == end:
        paths.append((path, weight))
        return
    
    visited.add(current)
    for dest in graph[current]:
        if dest not in visited:
            new_path = path + [dest]
            new_weight = weight + graph[current][dest]
            recurDFS(graph, dest, end, new_path, new_weight, visited, paths)
    visited.remove(current)


if __name__ == "__main__":
    main()
