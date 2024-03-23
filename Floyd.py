def floyd_warshall(n, edges):
    dist = [[float('inf')] * n for _ in range(n)]


    for u, v, w in edges:
        dist[u][v] = w
        dist[v][u] = w


    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist



n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u - 1, v - 1, w))  # 转换为0-indexed

# 计算并输出结果
dist_matrix = floyd_warshall(n, edges)
for row in dist_matrix:
    print(*row)