graph = {
    "A":["B","E"],
    "B":["A","C"],
    "C":["B","D","J"],
    "D":["C"],
    "E":["A","F","G"],
    "F":["E","I"],
    "G":["E","H"],
    "H":["G","I"],
    "I":["F","H","J","K"],
    "J":["C","I","K"],
    "K":["I","J"]
}

def BFS(graph,s):
    queue = []
    queue.append(s)
    seen = set()
    seen.add(s)
    parent = {s:None}
    
    while(len(queue) > 0):
        vertex  = queue.pop(0)
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
                parent[w] = vertex
        print(vertex)
    return parent

parent = BFS(graph,"A")
for key in parent:
    print(key,parent[key])

# 最短路径寻找
v = "J"
while v != None:
    print(v)
    v = parent[v]
