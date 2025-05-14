graph = [
    # список смежности
    [1],  # 0
    [0, 4],  # 1
    [5],  # 2
    [4],  # 3
    [1, 3, 7, 5],  # 4
    [2],  # 5
    [],  # 6
    [4, 8],  # 7
    [7],   #8
]
objects = {
    'bank': 3,
    'shop': 5,
    'bar': 8,
    'market': 6
}
home = 1

def dfs(graph, start):
    visited = [False] * len(graph)

    def _dfs(v):
        visited[v] = True
        for w in graph[v]:
            if not visited[w]:  # посещён ли текущий сосед?
                _dfs(w)

    _dfs(start)
    return visited

result = dfs(graph, home)

for name, vertex in objects.items():
    if result[vertex]:
        print(f"Сan go to the {name}")
    else:
        print(f"Сan't go to the {name}")