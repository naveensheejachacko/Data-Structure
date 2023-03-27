def add_node(v):
    if v in graph:
        print(v,"is present in graph")
    else:
        graph[v]=[]
def add_edge(v1,v2,cost):
    if v1 not in graph:
        print(v1,"is not present")
    elif v2 not in graph:
        print(v2,"is not present")
    else:
        list1=[v2,cost]
        list2=[v1,cost]
        graph[v1].append(list1)
        graph[v2].append(list2)
        
graph={}
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_edge("A","B",10)
add_edge("A","C",5)
print(graph)