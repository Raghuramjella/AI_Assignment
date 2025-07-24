class BridgeState:
    people = {
        'Amogh': 5,
        'Ameya': 10,
        'Grandmother': 20,
        'Grandfather': 25
    }

    def __init__(self, left, right, time, torch_side):
        self.left = left
        self.right = right
        self.time = time
        self.torch = torch_side

    def goalTest(self):
        return len(self.left) == 0 and len(self.right) == 4 and self.time <= 60

    def moveGen(self):
        children = []
        if self.torch == 'L':
            group = list(self.left)
            for i in range(len(group)):
                for j in range(i, len(group)):
                    cross = {group[i], group[j]}
                    new_left = self.left - cross
                    new_right = self.right | cross
                    cost = max(self.people[group[i]], self.people[group[j]])
                    new_time = self.time + cost
                    if new_time <= 60:
                        children.append(BridgeState(new_left, new_right, new_time, 'R'))
        else:
            group = list(self.right)
            for p in group:
                cross = {p}
                new_left = self.left | cross
                new_right = self.right - cross
                new_time = self.time + self.people[p]
                if new_time <= 60:
                    children.append(BridgeState(new_left, new_right, new_time, 'L'))
        return children

    def __eq__(self, other):
        return isinstance(other, BridgeState) and                self.left == other.left and self.right == other.right and                self.time == other.time and self.torch == other.torch

    def __hash__(self):
        return hash((frozenset(self.left), frozenset(self.right), self.time, self.torch))

    def __repr__(self):
        return f"L:{self.left}, R:{self.right}, T:{self.time}, Torch:{self.torch}"
