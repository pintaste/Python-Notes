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


def DFS(graph,s):
    stack = []
    stack.append(s)
    seen = set()
    seen.add(s)
    parent = {s:None}
    
    while(len(stack) > 0):
        vertex  = stack.pop()
        nodes = graph[vertex]
        for w in nodes:
            if w not in seen:
                stack.append(w)
                seen.add(w)
                parent[w] = vertex
        print(vertex)
    return parent


parent = DFS(graph,"A")
for key in parent:
    print(key,parent[key])
