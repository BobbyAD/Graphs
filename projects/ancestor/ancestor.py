class Vertex:
    def __init__(self, id, parents):
        self.parents = parents


def earliest_ancestor(ancestors, starting_node):
    vertexes = {}
    for i in ancestors:
        if i[1] in vertexes:
            vertexes[i[1]].parents.append(i[0])
        else:
            vertexes[i[1]] = Vertex(i[1], [i[0]])
    
    