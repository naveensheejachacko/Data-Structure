def add_node(v):
    if v in graph:
        print(v," is present")
    else:
        graph[v]=[]
def add_edge(v1,v2,cost):
    if v1 not in graph:
        print(v1,"is not present")
    if v2 not in graph:
        print(v2,"is not present")
    else:
        list1=[v2,cost]
        graph[v1].append(list1)

graph={}
add_node("A")
add_node("B")
add_node("C")
add_edge("A","B",10)
add_edge("A","C",5)
add_edge("B","C",3)
print(graph)