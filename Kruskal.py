parent = dict()
rank = dict()

# 초기화 함수
def make_reset(vertice):
	parent[vertice] = vertice
	rank[vertice] = 0

# 최상위 정점 찾는 함수
def find_root(vertice):
	if parent[vertice] != vertice:
		parent[vertice] = find_root(parent[vertice])
	return parent[vertice]

# 두 개의 정점을 연결하는 함수
def union_node(vertice1, vertice2):
	node1 = find_root(vertice1)
	node2 = find_root(vertice2)

	if node1 != node2:
		if rank[node1] > rank[node2]:
			parent[node2] = node1
		else:
			parent[node1] = node2
			if rank[node1] == rank[node2]:
				rank[node2] +=1

# Kruskal 
def mst_kruskal(graph):
	min_spanning_tree = []

	# 초기화
	for v in graph['vertices']:
		make_reset(v)

	# 간선 weight sorting
	edges = graph['edges']
	edges.sort()

	# 간선 연결 (사이클 없도록)
	for edge in edges:
		weight, vertice1, vertice2 = edge
		if find_root(vertice1) != find_root(vertice2):
			union_node(vertice1, vertice2)
			min_spanning_tree.append(edge)
			print(min_spanning_tree)
	return min_spanning_tree

graph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
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
