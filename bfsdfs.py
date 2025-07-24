from collections import deque

def bfs(start):
    OPEN = [(start, None)]
    CLOSED = []
    while OPEN:
        node_pair = OPEN.pop(0)
        N, parent = node_pair

        if N.goalTest():
            print("Goal is found")
            path = reconstructPath(node_pair, CLOSED)
            path.reverse()
            for node in path:
                print(node, "->", end=" ")
            print()
            return path
        else:
            CLOSED.append(node_pair)
            children = N.moveGen()
            new_nodes = removeSeen(children, OPEN, CLOSED)
            new_pairs = [(node, N) for node in new_nodes]
            OPEN = OPEN + new_pairs
    return []

def dfs(start):
    OPEN = [(start, None)]
    CLOSED = []
    while OPEN:
        node_pair = OPEN.pop(0)
        N, parent = node_pair

        if N.goalTest():
            print("Goal is found")
            path = reconstructPath(node_pair, CLOSED)
            path.reverse()
            for node in path:
                print(node, "->", end=" ")
            print("\n")
            return path
        else:
            CLOSED.append(node_pair)
            children = N.moveGen()
            new_nodes = removeSeen(children, OPEN, CLOSED)
            new_pairs = [(node, N) for node in new_nodes]
            OPEN = new_pairs + OPEN  
    return []


def reconstructPath(goal_node_pair, CLOSED):
    parent_map = {}
    for node, parent in CLOSED:
        parent_map[node] = parent

    path = []
    goal_node, parent = goal_node_pair
    path.append(goal_node)
    while parent is not None:
        path.append(parent)
        parent = parent_map[parent]
    return path

def removeSeen(children, OPEN, CLOSED):
    open_nodes = [node for node, parent in OPEN]
    closed_nodes = [node for node, parent in CLOSED]
    new_nodes = [c for c in children if c not in open_nodes and c not in closed_nodes]
    return new_nodes


