import heapq

moves = [(-1, 0), (1, 0), (0, -1), (0, 1),
         (-1, -1), (-1, 1), (1, -1), (1, 1)]

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def valid(x, y, n):
    return 0 <= x < n and 0 <= y < n

def best_first_search(grid):
    n = len(grid)
    start = (0, 0)
    goal = (n-1, n-1)
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1, []
    pq = []
    heapq.heappush(pq, (heuristic(start, goal), start))
    parent = {start: None}
    visited = set()
    while pq:
        _, node = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)
        if node == goal:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            path.reverse()
            return len(path), path
        x, y = node
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if valid(nx, ny, n) and grid[nx][ny] == 0 and (nx, ny) not in parent:
                parent[(nx,ny)] = (x,y)
                heapq.heappush(pq, (heuristic((nx, ny), goal), (nx, ny)))
    return -1, []

def a_star_search(grid):
    n = len(grid)
    start = (0, 0)
    goal = (n-1, n-1)
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1, []
    pq = []
    heapq.heappush(pq, (heuristic(start, goal), 0, start))
    parent = {start: None}
    g_cost = {start: 0}
    while pq:
        _, g, node = heapq.heappop(pq)
        if node == goal:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            path.reverse()
            return len(path), path
        x, y = node
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if valid(nx, ny, n) and grid[nx][ny] == 0:
                new_g = g + 1
                if (nx, ny) not in g_cost or new_g < g_cost[(nx, ny)]:
                    g_cost[(nx, ny)] = new_g
                    f = new_g + heuristic((nx, ny), goal)
                    parent[(nx, ny)] = (x, y)
                    heapq.heappush(pq, (f, new_g, (nx, ny)))
    return -1, []

if __name__ == "__main__":
    n = int(input("Enter grid size: "))
    print("Enter grid (each row with space separated 0/1):")
    grid = [list(map(int, input().split())) for _ in range(n)]
    bfs_len, bfs_path = best_first_search(grid)
    print("\nBest First Search → Path length:", bfs_len, ", Path:", bfs_path if bfs_len != -1 else "")
    astar_len, astar_path = a_star_search(grid)
    print("A* Search         → Path length:", astar_len, ", Path:", astar_path if astar_len != -1 else "")
