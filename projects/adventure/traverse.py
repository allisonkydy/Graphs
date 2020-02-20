

# def traverse_map(graph):
#     room_graph = {}
#     for i in graph:
#         room_graph[i] = graph[i][1]

#     path = []

#     # create a room_graph (destroyable)
#     # create empty list for the path
#     # create empty visited dict
#     # create empty queue

#     # start at room 0
#     # add room 0 to queue, along with its directions

#     # while length of visited is less than length of original graph
#         # dequeue room
#         # grab directions available from room
#         # check if any directions available to move
#             # if so, 

#     return path

def is_unexplored(graph):
    for room in graph:
        if '?' in graph[room].values():
            return True
    return False

def find_unexplored(room):
    for direction in room:
        if room[direction] == '?':
            return direction


def traverse_map(player):
    path = []
    starting_room = player.current_room.id
    graph = {}

    graph[starting_room] = {}
    for e in player.current_room.get_exits():
        graph[starting_room][e] = '?'

    # print(graph)
    reverse_directions = { 'n': 's', 's': 'n', 'e': 'w', 'w': 'e' }

    # while there are unexplored paths in graph
    while is_unexplored(graph):
        print("graph", graph)
        current_room = player.current_room.id
        print("current room", current_room)
        # check if current room has unexplored paths
        if '?' in graph[current_room].values():
        # if so,
            # find an unexplored direction from current room
            direction = find_unexplored(graph[current_room])
            print("direction", direction)
            # travel in that direction
            player.travel(direction)
            next_room = player.current_room.id
            print("next room", next_room)
            # add direction to path
            path.append(direction)
            # add directions to graph (replace '?'s)
            graph[current_room][direction] = player.current_room.id
            if not next_room in graph:
                graph[next_room] = {}
                for e in player.current_room.get_exits():
                    graph[next_room][e] = '?'
            graph[next_room][reverse_directions[direction]] = current_room
        # if no paths left,
            # perform a bfs to find nearest room with unexplored path ('?')

            # create empty queue
            # enqueue path to starting room
            # create empty visited set

            # while the queue is not empty...
                # dequeue path
                # grab last room from path
                # check if room has any unexplored exits
                # if so,
                    # convert path to unexplored room into list of directions
                    # add directions to traversal path
                    # move player to room using directions
                    # break loop
                # if not,
                    # enqueue paths to neighboring rooms
    
    return path