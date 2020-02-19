class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


def build_graph(ancestors):
    graph = dict()
    # for each pair in ancestors
    for pair in ancestors:
        # insert using the child as key and parent as value
        if pair[1] not in graph:
            graph[pair[1]] = set()
        if pair[0] not in graph:
            graph[pair[0]] = set()
        graph[pair[1]].add(pair[0])
    return graph


def earliest_ancestor(ancestors, starting_node):
    # create graph
    ancestor_graph = build_graph(ancestors)
    # create an empty stack
    s = Stack()
    # push path to starting node to stack
    s.push([starting_node])
    # keep track of path to earliest ancestor
    earliest_path = None
    # while the stack is not empty
    while s.size() > 0:
        # pop off a path from the stack
        path = s.pop()
        # grab the last node from the path
        node = path[-1]
        parents = ancestor_graph.get(node)
        # check if node has parents
        if len(parents) > 0:
            # if so, push all parents to stack
            for parent in parents:
                # copy path and add parent to new path
                path_copy = path.copy()
                path_copy.append(parent)
                s.push(path_copy)
        elif node == starting_node:
            continue
        # if no earliest ancestor saved yet OR
        # length of path to ancestor is less than current path OR
        # length of path to ancestor is equal to the current path AND earliest node value is greater than current node value
        elif earliest_path is None or len(earliest_path) < len(path) or (len(earliest_path) == len(path) and earliest_path[-1] > node):
            # set earliest path to path to current node
            earliest_path = path

    # check if starting node has no parents
    if earliest_path is None:
        return -1

    return earliest_path[-1]


# a1 = [(2, 1), (3, 1), (5, 2), (8, 3), (6, 8)]
# print(earliest_ancestor(a1, 1))