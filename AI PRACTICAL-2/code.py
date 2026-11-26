from collections import deque
import heapq

# Graph representation
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('D', 2), ('E', 5)],
    'C': [('A', 4), ('E', 1)],
    'D': [('B', 2), ('G', 3)],
    'E': [('B', 5), ('C', 1), ('G', 1)],
    'G': [('D', 3), ('E', 1)]
}

# Calculate total cost of a path
def path_cost(path):
    cost = 0
    for i in range(len(path) - 1):
        for node, weight in graph[path[i]]:
            if node == path[i + 1]:
                cost += weight
                break
    return cost


# Breadth-First Search
def bfs(start, goal):
    queue = deque([[start]])
    visited = set([start])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])

    return None


# Depth-First Search
def dfs(start, goal):
    stack = [[start]]
    visited = set()

    while stack:
        path = stack.pop()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)

            # Reverse order maintains a predictable traversal
            for neighbor, weight in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(path + [neighbor])

    return None


# Uniform-Cost Search
def ucs(start, goal):
    priority_queue = [(0, [start])]
    best_cost = {start: 0}

    while priority_queue:
        cost, path = heapq.heappop(priority_queue)
        node = path[-1]

        if node == goal:
            return path, cost

        if cost > best_cost.get(node, float('inf')):
            continue

        for neighbor, weight in graph[node]:
            new_cost = cost + weight

            if new_cost < best_cost.get(neighbor, float('inf')):
                best_cost[neighbor] = new_cost

                heapq.heappush(
                    priority_queue,
                    (new_cost, path + [neighbor])
                )

    return None, float('inf')


# Main program
start = 'A'
goal = 'G'

bfs_path = bfs(start, goal)
dfs_path = dfs(start, goal)
ucs_path, ucs_cost = ucs(start, goal)

print("BFS Path:", bfs_path)
print("BFS Cost:", path_cost(bfs_path))

print("\nDFS Path:", dfs_path)
print("DFS Cost:", path_cost(dfs_path))

print("\nUCS Path:", ucs_path)
print("UCS Cost:", ucs_cost)
