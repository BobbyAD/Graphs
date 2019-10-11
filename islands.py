# Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:

# islands = [[0, 1, 0, 1, 0],
#             [1, 1, 0, 1, 1],
#             [0, 0, 1, 0, 0],
#             [1, 0, 1, 0, 0],
#             [1, 1, 0, 0, 0]]

islands =  [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
            [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
            [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
            [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
            [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
            [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
            [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
            [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
            [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]

# island_counter(islands) # returns 4

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

def island_counter(islands):
    # visited cache
    # count of islands
    visited = set()
    island_count = 0
    q = Queue()
    for y in range(0, len(islands)):
        for x in range(0, len(islands[y])):
            if islands[y][x] == 1 and (y,x) not in visited:
                island_count += 1
                q.enqueue([y,x])
                visited.add((y,x))
                while q.size() > 0:
                    v = q.dequeue()
                    y_cord = v[0]
                    x_cord = v[1]
                    if y_cord > 0:
                        if (y_cord-1, x_cord) not in visited and islands[y_cord-1][x_cord] == 1:
                            visited.add((y_cord-1, x_cord))
                            q.enqueue([y_cord-1, x_cord])
                    if y_cord < len(islands)-1:
                        if (y_cord+1, x_cord) not in visited and islands[y_cord+1][x_cord] == 1:
                            visited.add((y_cord+1, x_cord))
                            q.enqueue([y_cord+1, x_cord])
                    if x_cord < len(islands[y_cord])-1:
                        if (y_cord, x_cord+1) not in visited and islands[y_cord][x_cord+1] == 1:
                            visited.add((y_cord, x_cord+1))
                            q.enqueue([y_cord, x_cord+1])
                    if x_cord > 0:
                        if (y_cord, x_cord-1) not in visited and islands[y_cord][x_cord-1] == 1:
                            visited.add((y_cord, x_cord-1))
                            q.enqueue([y_cord, x_cord-1])
    
    return island_count

print(island_counter(islands))