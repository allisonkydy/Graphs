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
    # keep track of earliest ancestor
    earliest = None
    longest_path = None
    # while the stack has nodes
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
        # if not, node is an ancestor
        else:
            if node == starting_node:
                continue
            # if earliest is None OR 
            # longest_path is less than current path OR 
            # longest path is equal to the current path AND earliest is greater than current node value
            if earliest is None or longest_path < len(path) or (longest_path == len(path) and earliest > node):
                # set earliest to current node
                earliest = node
                # set longest path to length of path
                longest_path = len(path)

    # check if starting node has no parents
    if earliest is None:
        return -1

    return earliest
                    