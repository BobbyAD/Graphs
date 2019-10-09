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

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(0, numUsers):
            self.addUser(f"{i}")

        calls = 0

        # Create friendships
        for u in self.users:
            for f in range(0, random.randint(0, avgFriendships)):
                friend = random.randint(1,numUsers)
                # Reroll if the friendship already exists or it's the same as the user we're adding friends to
                while friend in self.friendships[u] or friend is u:
                    friend = random.randint(1,numUsers)
                self.addFriendship(u, friend)
                calls += 1

        print("Calls to addFriendship")
        print(calls)

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        q = Queue()

        q.enqueue([userID])

        #BFT
        while q.size() > 0:
            path = q.dequeue()
            vertex = path[-1]
            if vertex in visited:
                #This doesn't ever actually execute because BFT hits shortest path first
                #Good boilerplate for swapping to see longest path, though
                if len(path) < len(visited[vertex]):
                    visited[vertex] = path.copy()
            else:
                for friend in self.friendships[vertex]:
                    visited[vertex] = path.copy()
                    path_copy = path.copy()
                    path_copy.append(friend)
                    q.enqueue(path_copy)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(1000, 5)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)

    """
    Sanity check for averages
    """
    total = 0
    for i in range(1, len(sg.friendships)+1):
        total += len(sg.friendships[i])

    total /= len(sg.friendships)
    print("Average Friendships")
    print(total)

    """
    Average degrees of seperation
    """
    total = 0
    avg_sep = 0
    for i in range(1, len(sg.friendships)+1):
        con = sg.getAllSocialPaths(i)
        total += len(con)

        cur_sep_avg = 0
        for i in con:
            cur_sep_avg += len(con[i])

        if cur_sep_avg > 0:
            cur_sep_avg /= len(con)
        avg_sep += cur_sep_avg


    total /= len(sg.friendships)
    print("Average Connections")
    print(total)

    avg_sep /= len(sg.friendships)
    print("Average Degrees of Seperation")
    print(avg_sep)


"""
    To create 100 users with an average of 10 friends each, how many times would you need to call addFriendship()? Why?
        500ish - As I grow the list of connections, I don't have to make as many towards the end of the list where they're already connected.
    If you create 1000 users with an average of 5 random friends each, what percentage of other users will be in a particular user's extended social network? What is the average degree of separation between a user and those in his/her extended network?
        Almost every user (97ish percent) will be in their friend network with an average degree of seperation of 5. 
"""