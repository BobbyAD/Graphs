# class Vertex:
#     def __init__(self, id, parents):
#         self.parents = parents


# def earliest_ancestor(ancestors, starting_node):
#     def recursive_find(vertexes, starting_node, path = []):
#         path.append(starting_node)
#         if starting_node in vertexes:
#             new_list = []
#             for i in vertexes[starting_node].parents:
#                 returned_list = recursive_find(vertexes, i, path.copy())
#                 if len(returned_list) > len(new_list):
#                     new_list = returned_list
#                 elif len(returned_list) == len(new_list):
#                     if returned_list[-1] < new_list[-1]:
#                         new_list = returned_list
#             return new_list
#         else:
#             return path
#     #One way paths going up family tree
#     vertexes = {}
#     for i in ancestors:
#         if i[1] in vertexes:
#             vertexes[i[1]].parents.append(i[0])
#         else:
#             vertexes[i[1]] = Vertex(i[1], [i[0]])
    
#     if starting_node not in vertexes:
#         return -1
    
#     longest_branch = recursive_find(vertexes, starting_node)

#     print(longest_branch)

#     return longest_branch[-1]


# Class solution
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
    
class Graph():
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
            #TODO: Do we need error checking here?
        
    def add_edges(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])

        #Link from kids to parents
        graph.add_edges(pair[1], pair[0])
    
    q = Queue()
    q.enqueue([starting_node])

    max_path_length = 1
    earliest_ancestor = -1

    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]

        if (len(path) > max_path_length) or (len(path) == max_path_length and v < earliest_ancestor):
            earliest_ancestor = v
            max_path_length = len(path)

        for neighbor in graph.vertices[v]:
            path_copy = list(path)
            path_copy.append(neighbor)
            q.enqueue(path_copy)

    return earliest_ancestor