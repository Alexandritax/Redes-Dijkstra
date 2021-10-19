import sys
import concurrent.futures


#definimos como fuente el nodo incial del grafo
#los otros nodos los llamare vertices

class Graph():
    def __init__(self,vertices): #inicializando con los vertices
        self.V=vertices
        self.graph = [[0 for columnas in range(vertices) 
        for lineas in range(vertices)]] #queremos una matriz cuadrada

    def printSolucion(self,dist,src): #dist es la lista de distancias
        print("Distancia de los vertices desde el nodo {}".format(src))
        for node in range(self.V):
            print("router" ,node, "--> ", dist[node])
    
    def minDistance(self,dist,sptSet):
        min = sys.maxsize
        
        for v in range(self.V):
            if dist[v]< min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index
    
    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False]*self.V

        for cout in range(self.V):

            u = self.minDistance(dist, sptSet)
            
            sptSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolucion(dist,src)


def main():
    g = Graph(9)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]
 
    with concurrent.futures.ProcessPoolExecutor() as executor:
        nodes = [i for i in range(9)]
        executor.map(g.dijkstra,nodes)

if __name__ == "__main__":
    main()

