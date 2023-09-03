cities, roads = map(int, input().split())
graph = []
for i in range(roads):
    graph.append(list(map(int, input().split())))


def graph_to_traversal_form(graph):
    g= {}
    for edge in graph:
        g[edge[0]] = g.get(edge[0], set()) | {edge[1]}
        g[edge[1]] = g.get(edge[1], set()) | {edge[0]}
    return g

trav_graph = graph_to_traversal_form(graph)


def count_connected_components(graph, nodes):
    count = 0
    visited = set()

    for node in nodes:
        if node not in visited:
            count += 1
            stack = [node]

            while stack:
                current_node = stack.pop()
                visited.add(current_node)

                for neighbor in graph[current_node]:
                    if neighbor not in visited:
                        stack.append(neighbor)

    return count


class DisjointSet:
    def __init__(self, vertices, ):
        self.vertices = vertices
        self.parent = {}
        for v in vertices:
            self.parent[v] = v
        self.rank = dict.fromkeys(vertices, 0)

    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            return self.find(self.parent[item])
    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        elif self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1

def kruskal(graph, ):
    min_tree=[]
    graph = sorted(graph, key=lambda x: x[2], reverse=True)
    i, e = 0, 0
    s = set()
    for edge in graph:
        s.add(edge[0])
        s.add(edge[1])
    ds = DisjointSet(s)

    trav_graph = graph_to_traversal_form(graph)

    states = count_connected_components(trav_graph,s)

    max_weight = graph[0][2]
    count = 0
    while e< (len(s)-states):

        source, dest, weight = graph[i]
        i += 1
        x = ds.find(source)
        y = ds.find(dest)
        if x != y:
            e += 1
            count+=1

            ds.union(x, y)
            if weight < max_weight:

                max_weight = weight


    if count == 0:
        print(max_weight)
    else:
        print(max_weight-1)

kruskal(graph)