def main():
    vertex_count, edge_count = [int(x) for x in input().split()]

    adj_list = {}
    start = None
    for i in range(edge_count):
        u, v, w = [x for x in input().split()]

        if not start:
            start = u

        if u not in adj_list:
            adj_list[u] = {v: int(w)}
        else:
            adj_list[u][v] = int(w)

    total, path = greedy_search(adj_list, start)
    print(total)
    for i in path:
        if i != path[0]:
            print(end=" ")
        print(i, end="")
    print()


def greedy_search(adj_list, start):
    visited = set()
    path = [start]
    total = 0

    while len(visited) < len(adj_list) - 1:
        if start not in adj_list:
            break
        max = -1
        max_vertex = None
        for j in adj_list[start]:
            if adj_list[start][j] > max and j not in visited:
                max = adj_list[start][j]
                max_vertex = j
        if not max_vertex:
            break
        visited.add(max_vertex)
        path.append(max_vertex)
        total += max
        start = max_vertex
    return total, path

if __name__ == "__main__":
    main()