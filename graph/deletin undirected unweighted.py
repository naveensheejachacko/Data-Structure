def add_node(v):
    if v in graph:
        print(v,"is present")
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
def delete_node(v):
    if v not in graph:
        print(v,"not prsent")
    else:
        graph.pop(v)
        for i in graph:
            list1=graph[i]
            if v in list1:
                list1.remove(v)
def delete_edge(v1,v2):
    if v1 not in graph:
        print(v1,"is not present")
    elif v2 not in graph:
        print(v2," is not present ")
    else:
        if v2 in graph[v1]:
            graph[v1].remove(v2)
            graph[v2].remove(v1)

graph={}
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_node("A")
add_edge('A','B')
add_edge('A','C')
add_edge('C','D')
add_edge('D','E')
print(graph)
delete_node("A")
delete_edge("A","D")
print(graph)