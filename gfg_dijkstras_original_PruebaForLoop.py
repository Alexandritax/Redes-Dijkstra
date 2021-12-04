# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph

# Library for INT_MAX
import sys
import numpy as np
import time

class Graph():
	def __init__(self, vertices):
		self.V = vertices
		self.graph = [[0 for column in range(vertices)]
		for row in range(vertices)]

	def printSolution(self, dist, src):
		print(f"Vertex t Distance from Source {src}")
		print(f"size de los resultados: {sys.getsizeof(dist)}")
		for node in range(self.V):
    			if(dist[node]!=0):
    				print("\trouter" ,node, "--> ", dist[node])
            

	# A utility function to find the vertex with
	# minimum distance value, from the set of vertices
	# not yet included in shortest path tree
	def minDistance(self, dist, sptSet):
		# Initialize minimum distance for next node
		min = sys.maxsize
		# Search not nearest vertex not in the
		# shortest path tree
		for v in range(self.V):
			if dist[v] < min and sptSet[v] == False:
				min = dist[v]
				min_index = v

		return min_index

	# Funtion that implements Dijkstra's single source
	# shortest path algorithm for a graph represented
	# using adjacency matrix representation
	def dijkstra(self, src):
		dist = [sys.maxsize] * self.V
		dist[src] = 0
		sptSet = [False] * self.V

		for cout in range(self.V):

			# Pick the minimum distance vertex from
			# the set of vertices not yet processed.
			# u is always equal to src in first iteration
			u = self.minDistance(dist, sptSet)

			# Put the minimum distance vertex in the
			# shortest path tree
			sptSet[u] = True

			# Update dist value of the adjacent vertices
			# of the picked vertex only if the current
			# distance is greater than new distance and
			# the vertex in not in the shortest path tree
			for v in range(self.V):
				if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]: dist[v] = dist[u] + self.graph[u][v]

		self.printSolution(dist, src)



start_g = time.time()
g = Graph(8)
print("Grafo de baja complejidad:\n")
g.graph = np.loadtxt("Baja_complejidad.txt",skiprows=0).astype(int)
for i in range(g.V):
	g.dijkstra(i)
fin_g= time.time()
low_time = fin_g-start_g
print(f'Time in low complexity = {low_time}')
print("---------------------------------------------------\n")
print("Grafo de alta complejidad:\n")
start_h=time.time()
h = Graph(11)
h.graph = np.loadtxt("Alta_complejidad.txt",skiprows=0).astype(int)
for k in range(h.V):
	h.dijkstra(k)
fin_h = time.time()
high_time = fin_h-start_h
print(f'Time in high complexity = {high_time}')
print(f"Tiempo total: {high_time+low_time}")
# This code is contributed by Divyanshu Mehta
# Se usa el codigo original para verificar la ejecucion del codigo via for.