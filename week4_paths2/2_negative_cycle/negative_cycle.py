# Uses python3

import sys


def negative_cycle(adj, costs):
    # write your code here
    dist = dict()
    prev = dict()
    visited = [False] * len(adj)

    for i, node in enumerate(adj):
        dist[i] = float('inf')
        prev[i] = None

    for x in range(len(adj)):
        if not visited[x]:
            dist[x] = 0
            for _ in range(len(adj)):
                for i, node in enumerate(adj):
                    for edge, cost in zip(node, costs[i]):
                        if dist[edge] > dist[i] + cost:
                            dist[edge] = dist[i] + cost
                            prev[edge] = i

            print(dist)

            for i, node in enumerate(adj):
                for edge, cost in zip(node, costs[i]):
                    if dist[edge] > dist[i] + cost:
                        return 1

            for i in range(len(adj)):
                if dist[i] != float('inf'):
                    visited[i] = True

    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
