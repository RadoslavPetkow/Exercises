import heapq
from collections import defaultdict

def maxProbability(n, edges, succProb, start, end):
    # Create the graph as an adjacency list
    graph = defaultdict(list)
    for i, (a, b) in enumerate(edges):
        prob = succProb[i]
        graph[a].append((b, prob))
        graph[b].append((a, prob))

    # List to track the maximum probability to each node
    max_prob = [0.0] * n
    max_prob[start] = 1.0

    # Priority queue (max-heap simulated using negative values)
    pq = [(-1.0, start)]

    while pq:
        # Extract node with current highest probability
        prob, node = heapq.heappop(pq)
        prob = -prob

        # If we reach the end node, return the probability
        if node == end:
            return prob

        # Check neighbors
        for neighbor, edge_prob in graph[node]:
            new_prob = prob * edge_prob
            if new_prob > max_prob[neighbor]:
                max_prob[neighbor] = new_prob
                heapq.heappush(pq, (-new_prob, neighbor))

    return 0.0

# Example usage:
n = 3
edges = [[0, 1], [1, 2], [0, 2]]
succProb = [0.5, 0.5, 0.2]
start = 0
end = 2

print(maxProbability(n, edges, succProb, start, end))