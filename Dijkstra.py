INF = 999

def choose_vertex(dist, found):
	min_dist = INF
	min_pos = -1
	for i in range(len(dist)):
		if dist[i] < min_dist and found[i] == False:
			min_dist = dist[i]
			min_pos = i
	return min_pos

def dijkstra(vtx, adj, start):
	v_size = len(vtx)	    # 정점의 수
	dist = list(adj[start])     # 시작 정점으로부터 최단 경로 거리 저장
	path = [start] * v_size     # 바로 이전 정점 저장. 이전 정점을 따라 시작 정점까지 가는 경로가 최단 경로
	found = [False] * v_size    # 방문한 정점 표. 최초 False 설정
	dist[start] = 0

	for i in range(v_size):
		print("Step %2d: "%(i+1), dist)
		u = choose_vertex(dist, found)
		found[u] = True
	
		for w in range(v_size):
			if not found[w]:
				if dist[u] + adj[u][w] < dist[w]:
					dist[w] = dist[u] + adj[u][w]
					path[w] = u
	return path 
	
vertex = ["A", "B", "C", "D", "E", "F", "G"]
weight = [[0  , 7  , INF, INF, 3  , 10 , INF],
          [7  , 0  , 4  , 10 , 2  , 6  , INF],
          [INF, 4  , 0  , 2  , INF, INF, INF],
          [INF, 10 , 2  , 0  , 11 , 9  , 4  ],
          [3  , 2  , INF, 11 , 0  , 13 , 5  ],
          [10 , 6  , INF, 9  , 13 , 0  , INF],
          [INF, INF, INF, 4  , 5  , INF, 0  ]]

print("<Dijkstra Algorithm>")
start = 0
path = dijkstra(vertex, weight, start)

# 최종 경로 출력
for end in range(len(vertex)):
	if end != start:
		print("[최단 경로: %s => %s] %s" %(vertex[start], vertex[end], vertex[end]), end = ' ')
		while path[end] != start:
			print(" <= %s" %vertex[path[end]], end = ' ')
			end = path[end]
		print(" <= %s" %vertex[path[end]])
