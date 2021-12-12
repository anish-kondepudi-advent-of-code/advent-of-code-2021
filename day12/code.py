
def readfile(filename):
    with open(filename) as file:
        return [line.strip().split("-") for line in file.readlines()]

# PART 1

def dfs1(node,edges,visited):
    # Base Cases
    if node in visited: return 0
    if node == 'end': return 1
    # Mark as Visited
    if node == 'start' or node.islower():
        visited.add(node)
    # Recurse DFS
    numPaths = 0
    for u,v in edges:
        if node == u:
            newVisited = visited.copy()
            numPaths += dfs1(v,edges,newVisited)
        if node == v:
            newVisited = visited.copy()
            numPaths += dfs1(u,edges,newVisited)
    # Return
    return numPaths


def findNumPaths1(filename):
    node = 'start'
    edges = readfile(filename)
    visited = set()
    return dfs1(node,edges,visited)


print(findNumPaths1("input.txt"))


# PART 2

def findSmallEdges(edges):
    V = set()
    for u,v in edges:
        V.add(u)
        V.add(v)
    smallEdges = []
    for v in V:
        if v != 'start' and v != 'end' and v.islower():
            smallEdges.append(v)
    return smallEdges


def dfs2(node,edges,visited,path,paths,biedge):
    # Base Cases
    path += "->"+node
    if node in visited: return 0
    if node == 'end': 
        paths.add(path)
        return 1
    # Mark as Visited
    if node == 'start' or node.islower():
        visited.add(node)
    if node == biedge:
        visited.remove(node)
        biedge = ""
    # Recurse DFS
    numPaths = 0
    for u,v in edges:
        if node == u:
            newVisited = visited.copy()
            numPaths += dfs2(v,edges,newVisited,path,paths,biedge)
        if node == v:
            newVisited = visited.copy()
            numPaths += dfs2(u,edges,newVisited,path,paths,biedge)
    # Return
    return numPaths


def findNumPaths2(filename):
    edges = readfile(filename)
    smallEdges = findSmallEdges(edges)
    paths = set()
    for biedge in smallEdges:
        x = dfs2('start',edges,set(),"",paths,biedge)
    return len(paths)

print(findNumPaths2("input.txt"))

