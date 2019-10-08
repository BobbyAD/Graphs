class Vertex:
    def __init__(self, id, parents):
        self.parents = parents


def earliest_ancestor(ancestors, starting_node):
    def recursive_find(vertexes, starting_node, path = []):
        path.append(starting_node)
        if starting_node in vertexes:
            new_list = []
            for i in vertexes[starting_node].parents:
                returned_list = recursive_find(vertexes, i, path.copy())
                if len(returned_list) > len(new_list):
                    new_list = returned_list
            return new_list
        else:
            return path
    #One way paths going up family tree
    vertexes = {}
    for i in ancestors:
        if i[1] in vertexes:
            vertexes[i[1]].parents.append(i[0])
        else:
            vertexes[i[1]] = Vertex(i[1], [i[0]])
    
    if starting_node not in vertexes:
        return -1
    
    longest_branch = recursive_find(vertexes, starting_node)

    print(longest_branch)

    return longest_branch[-1]
    