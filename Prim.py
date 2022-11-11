INF = 9999   # 가장 큰 가중치

# 현재 트리에 인접한 정점들 중에서 가장 가까운 정점을 찾는 함수
def find_min_vertice(dist, selected):
	min_vertice = 0
	min_dist = INF
	for v in range(len(dist)):
		if not selected[v] and dist[v] < min_dist:
			min_dist = dist[v]
			min_vertice = v
	return min_vertice

# Prim
def mst_prim(vertice, adj):
	vertice_size = len(vertice)
	dist = [INF] * vertice_size
	selected = [False] * vertice_size
	dist[0] = 0
	
	for i in range(vertice_size):
		min_v = find_min_vertice(dist, selected)
		selected[min_v] = True
		print(vertice[min_v], end = ' ')

		for v in range(vertice_size):
			if adj[min_v][v] != None:
				if selected[v] == False and adj[min_v][v] < dist[v]:
					dist[v] = adj[min_v][v]
	print()

vertice_list = ["A", "B", "C", "D", "E", "F"]
weight = [ [None, 29  , None, None, None, 10  , None],
           [29  , None, 16  , None, None, None, 15  ],
           [None, 16  , None, 12  , None, None, None],
           [None, None, 12  , None, 22  , None, 18  ],
           [None, None, None, 22  , None, 27  , 25  ],
           [10  , None, None, None, 27  , None, None],
           [None, 15  , None, 18  , 25  , None, None]]

print("<Prim Algorithm>")
mst_prim(vertice_list, weight)

