from rabbit import RabbitState
from bridge import BridgeState
from bfsdfs import bfs, dfs

# Rabbit Problem
start_rabbit = RabbitState("EEE_OOO")
bfs(start_rabbit)
dfs(start_rabbit)

# Bridge Problem
start_bridge = BridgeState({'Amogh', 'Ameya', 'Grandmother', 'Grandfather'}, set(), 0, 'L')
bfs(start_bridge)
dfs(start_bridge)
