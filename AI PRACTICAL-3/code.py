import heapq
# Goal state
goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


# Generate possible moves
def get_neighbors(state):
    neighbors = []

    zero = state.index(0)
    row = zero // 3
    col = zero % 3

    moves = [
        (-1, 0),   # Up
        (1, 0),    # Down
        (0, -1),   # Left
        (0, 1)     # Right
    ]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_zero = new_row * 3 + new_col

            new_state = list(state)

            new_state[zero], new_state[new_zero] = (
                new_state[new_zero],
                new_state[zero]
            )

            neighbors.append(tuple(new_state))

    return neighbors


# Heuristic 1: Misplaced Tiles
def misplaced_tiles(state):
    count = 0

    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1

    return count


# Heuristic 2: Manhattan Distance
def manhattan_distance(state):
    distance = 0

    for i in range(9):
        tile = state[i]

        if tile != 0:
            current_row = i // 3
            current_col = i % 3

            goal_index = goal.index(tile)

            goal_row = goal_index // 3
            goal_col = goal_index % 3

            distance += abs(current_row - goal_row)
            distance += abs(current_col - goal_col)

    return distance


# Check whether puzzle is solvable
def is_solvable(state):
    values = [x for x in state if x != 0]

    inversions = 0

    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if values[i] > values[j]:
                inversions += 1

    return inversions % 2 == 0


# A* Search
def a_star(start, heuristic):
    priority_queue = []

    g_cost = {start: 0}
    parent = {start: None}

    h = heuristic(start)

    heapq.heappush(
        priority_queue,
        (h, 0, start)
    )

    visited = set()

    while priority_queue:
        f, g, current = heapq.heappop(priority_queue)

        if current in visited:
            continue

        visited.add(current)

        # Goal reached
        if current == goal:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()

            return path, len(visited)

        # Generate next states
        for neighbor in get_neighbors(current):
            new_g = g + 1

            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                parent[neighbor] = current

                h = heuristic(neighbor)
                f = new_g + h

                heapq.heappush(
                    priority_queue,
                    (f, new_g, neighbor)
                )

    return None, len(visited)


# Display puzzle
def display(state):
    for i in range(0, 9, 3):
        print(state[i:i + 3])


# User input
print("Enter the 8-puzzle values")
print("Use 0 for blank space")

start = []

for i in range(9):
    while True:
        try:
            value = int(input("Enter value: "))

            if value not in range(9):
                print("Enter a number from 0 to 8.")
            elif value in start:
                print("Value already entered. Try again.")
            else:
                start.append(value)
                break

        except ValueError:
            print("Invalid input. Enter an integer.")

start = tuple(start)


# Display initial state
print("\nInitial Puzzle:")
display(start)


# Check solvability
if not is_solvable(start):
    print("\nThis puzzle is not solvable.")
else:

    # A* using Misplaced Tiles
    path1, nodes1 = a_star(
        start,
        misplaced_tiles
    )

    # A* using Manhattan Distance
    path2, nodes2 = a_star(
        start,
        manhattan_distance
    )

    # Result 1
    print("\n--- Misplaced Tiles Heuristic ---")

    if path1:
        print("Number of moves:", len(path1) - 1)
        print("Nodes explored:", nodes1)

        print("\nPath:")

        for state in path1:
            display(state)
            print()
    else:
        print("No solution found")

    # Result 2
    print("\n--- Manhattan Distance Heuristic ---")

    if path2:
        print("Number of moves:", len(path2) - 1)
        print("Nodes explored:", nodes2)

        print("\nPath:")

        for state in path2:
            display(state)
            print()
    else:
        print("No solution found")
