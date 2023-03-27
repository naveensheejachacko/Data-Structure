def add_node(v):
    if v in graph:
        print(v,"is present in graph")
    else:
        graph[v]=[]
def add_edges(v1,v2):
    if v1 not in graph:
        print(v1,"not present in graph")
    elif v2 not in graph:
        print(v2,"not present in graph")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)

graph={}

add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_node("A")
add_edges('A','B')
add_edges('A','C')
add_edges('C','D')
add_edges('D','E')
print(graph)