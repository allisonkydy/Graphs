import random

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class User:
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return self.name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(num_users):
            self.add_user(f"User {i}")

        # Create friendships

        # create a list of all possible friendships
        # possible_friendships = []
        # for user_id in self.users:
        #     for friend_id in range(user_id + 1, self.last_id + 1):
        #         possible_friendships.append((user_id, friend_id))
        # shuffle the list
        # random.shuffle(possible_friendships)


        # grab the first n friendship pairs from list and create those friendships
            # avg_friendships = total_friendships / num_users
            # total_friendships = avg_friendships * num_users
            # n = total_friendships // 2
            # n = avg_friendships * num_users // 2
        # for i in range(num_users * avg_friendships // 2):
        #     friendship = possible_friendships[i]
        #     self.add_friendship(friendship[0], friendship[1])

        # stretch---
        total_friendships = num_users * avg_friendships // 2
        # generate random friendships
        for i in range(total_friendships):
            user = random.randint(1, num_users)
            friend = random.randint(1, num_users)

            while user == friend or friend in self.friendships[user] or user in self.friendships[friend]:
                user = random.randint(1, num_users)
                friend = random.randint(1, num_users)

            self.add_friendship(user, friend)

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # use bft
        # create empty queue
        q = Queue()
        # enqueue path to staring user id
        q.enqueue([user_id])
        # while the queue is not empty...
        while q.size() > 0:
            # dequeue path to user
            path = q.dequeue()
            # grab user from end of path
            user = path[-1]
            # check if user in visited, if not...
            if user not in visited:
                # mark as visited (user is key, path is value)
                visited[user] = path
                # enqueue all neighbors
                for neighbor in self.friendships[user]:
                    # copy path and add neighbor 
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    q.enqueue(path_copy)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print("\nusers\n", sg.users)
    print("\nfriendships\n", sg.friendships)
    connections = sg.get_all_social_paths(1)
    print("\nconnections\n", connections)

    # for answer to question 2
    # sg = SocialGraph()
    # sg.populate_graph(1000, 5)
    # # print("\nfriendships\n", sg.friendships)
    # connections = sg.get_all_social_paths(1)
    # # print("\nconnections\n", connections)

    # degree_of_separation = 0
    # for i in range(1, 1001):
    #     if i in connections:
    #         degree_of_separation += len(connections[i])
    # percentage = (len(connections) / 1000) * 100
    # avg_degree_of_separation = degree_of_separation / len(connections)
    # print(f"\npercentage of users in extended social network of user 1: {percentage}%")
    # print(f"\naverage degree of separation between user and users in network: {avg_degree_of_separation}")

# Questions

# 1. To create 100 users with an average of 10 friends each, how many times would you need to call add_friendship()? Why?

# 500 times. 1000 total friendships need to be generated (100 users * 10 friends each), and calling add_friendships creates a bi-directional friendship - essentially creates two friendships - so calling it 500 times will create 1000 friendships. 

# 2. If you create 1000 users with an average of 5 random friends each, what percentage of other users will be in a particular user's extended social network? What is the average degree of separation between a user and those in his/her extended network?

# About 99 - 100% of other users will be in a particular user's extended social network (sometimes there will be a user without any connections). The average degree of separation is about 5 - 6 depending on the network. 

