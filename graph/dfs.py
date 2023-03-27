def add_node(v):
    if v in graph:
        print(v,"is already present")
    else:
        graph[v]=[]
def add_edge(v1,v2):
    if v1 not in graph:
        print(v1,"is not present")
    elif v2 not in graph:
        print(v2,"is not present")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)
def DFS(node,visted,graph):
    if node not in graph:
        print("node is not present")
        return
    if node not in visited:
        print(node)
        visted.add(node)
        for i in graph[node]:
            DFS(i,visited,graph)


graph={}
visited=set()
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_edge('A','B')
add_edge('A','C')
add_edge('A','D')
add_edge('D','B')
add_edge('D','C')
add_edge('B','E')
add_edge('E','D')
print(graph)
DFS("A",visited,graph)
