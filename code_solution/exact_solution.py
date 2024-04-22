"""
    name:  Jacob Susko
    Longest Path Exact Solution
    Directions for running:
"""


def main():
    one, two = input().split()
    num_verticies, num_edges = int(one), int(two)
    
    graph = {chr(97 + i): {} for i in range(num_verticies)}

    for _ in range(num_edges):
        a, b, c = input().split()
        graph[a][b] = int(c)

    print(graph)
    pass

if __name__ == "__main__":
    main()
