def add_node(v):
    if v in graph:
        print("node already present")
    else:
        graph[v]=[]
def add_edge(v1,v2):
    if v1 not in graph:
        print(v1,"node not present")

    elif v2 not in graph:
        print(v2,"node not present")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)
def DFSiterative(node,graph):
    if node not in graph:
        print("node not present in graph")
        return
    visited=set()
    stack=[]
    stack.append(node)
    while stack:
        current=stack.pop()
        if current not in visited:
            print(current,'-->',end=" ")
            visited.add(current)
            for i in graph[current]:
                stack.append(i)

graph={}
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
DFSiterative("B",graph)