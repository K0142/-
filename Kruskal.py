parent = dict()
rank = dict()

# 초기화 함수
def make_reset(vertex):
	parent[vertex] = vertex
	rank[vertex] = 0

# 최상위 정점 찾는 함수
def find_root(vertex):
	if parent[vertex] != vertex:
		parent[vertex] = find_root(parent[vertex])
	return parent[vertex]

# 두 개의 정점을 연결하는 함수
def union_node(vertex1, vertex2):
	vertex1 = find_root(vertex1)
	vertex2 = find_root(vertex2)

	if vertex1 != vertex2:
		if rank[vertex1] > rank[vertex2]:
			parent[vertex2] = vertex1
		else:
			parent[vertex1] = vertex2
			if rank[vertex1] == rank[vertex2]:
				rank[vertex2] +=1

# Kruskal 
def mst_kruskal(graph):
	min_spanning_tree = []

	# 초기화
	for v in graph['vertex']:
		make_reset(v)

	# 간선 weight sorting
	edges = graph['edges']
	edges.sort()

	# 간선 연결 (사이클 없도록)
	for edge in edges:
		weight, vertex1, vertex2 = edge
		if find_root(vertex1) != find_root(vertex2):
			union_node(vertex1, vertex2)
			min_spanning_tree.append(edge)
			print(min_spanning_tree)
	return min_spanning_tree

graph = {
    'vertex': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges': [
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (7, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F')
    ]
}

print("<Kruskal Algorithm>")
mst_kruskal(graph)
