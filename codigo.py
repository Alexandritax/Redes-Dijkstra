import sys #permite usar la funcion maxsize para representar un numero enorme.
import concurrent.futures


#definimos como fuente el nodo incial del grafo
#los otros nodos los llamare vertices
#https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/

class Graph():
    def __init__(self,vertices): #inicializando con los vertices
        self.V=vertices
        self.graph = [[0 for columnas in range(vertices) 
        for lineas in range(vertices)]] #queremos una matriz cuadrada

    def printSolucion(self,dist,src): #dist es la lista de distancias
        print("\tDistancia a los vertices desde el nodo {}".format(src))
        for node in range(self.V):
            if(node != src):
                print("\trouter" ,node, "--> ", dist[node])
        print("\n")
    
    def minDistance(self,dist,sptSet):
        min = sys.maxsize #peudo-infinito
        
        for v in range(self.V):
            if dist[v]< min and sptSet[v] == False: #si el nodo no fue visitado y la distancia sea menor al minimo.
                min = dist[v]
                min_index = v #retorna el nodo con la menor distancia

        return min_index
    
    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False]*self.V

        for _ in range(self.V):

            u = self.minDistance(dist, sptSet) # u sera el nodo con la menor distancias
            # Primero u sera el nodo fuente, dado que su distancia es 0
            
            sptSet[u] = True
            #se marca quien es el nodo fuente.

            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False and dist[u] + self.graph[u][v] < dist[v]: #buscara la distancia de los demas nodos desde el nodo fuente
                    #self.graph[u][v] > 0 una arista desde el nodo u y v exite si en el grafo tiene un valor mayor a 0 su distancia
                    # sptSet[v]==false no queremos trabajar con el nodo de origen.
                    # dist[u] + self.graph[u][v] < dist[v] busca que la nueva distancia sea menor a la distancia anterior.
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolucion(dist,src) #imprime las distancias


def main():
    print("Grafo de baja complejidad:\n")
    nodos_LC = 8
    Low_complexity = Graph(nodos_LC)
    Low_complexity.graph = [[0,3,4,0,0,0,0,0],
    [3,0,0,5,6,0,0,0],
    [4,0,0,0,2,3,0,0],
    [0,5,0,0,0,0,0,0],
    [0,6,2,0,0,0,4,5],
    [0,0,3,0,0,0,0,0],
    [0,0,0,0,4,0,0,1],
    [0,0,0,0,5,0,1,0]
    ]
 
    with concurrent.futures.ProcessPoolExecutor() as executor_LC: #crea un ejecutor de multi-procesos para el grafo de baja complejidad
        nodes = [i for i in range(nodos_LC)] 
        executor_LC.map(Low_complexity.dijkstra,nodes) #ejecuta dijkstra en varios procesos para todos los nodos paralelamente.
    print("---------------------------------------------------\n")
    print("Grafo de alta complejidad:\n")
    nodos_HC = 11
    High_complexity = Graph(nodos_HC)
    High_complexity.graph = [[0,6,5,0,0,0,0,0,0,0,0],
    [6,0,0,4,3,0,0,0,0,0,0], 
    [5,0,0,0,5,8,0,0,0,0,0], 
    [0,4,0,0,0,0,0,0,0,0,0], 
    [0,3,5,0,0,0,2,0,0,3,0],
    [0,0,8,0,0,0,0,0,0,0,3],
    [0,0,0,0,2,0,0,4,4,0,0],
    [0,0,0,0,0,0,4,0,0,0,0],
    [0,0,0,0,0,0,4,0,0,0,1],
    [0,0,0,0,3,0,0,0,0,0,0],
    [0,0,0,0,0,3,0,0,1,0,0]]

    with concurrent.futures.ProcessPoolExecutor() as executor_HC: #crea un ejecutor de multi-procesos para el grafo de alta complejidad
        nodes = [i for i in range(nodos_HC)] 
        executor_HC.map(High_complexity.dijkstra,nodes) #ejecuta dijkstra en varios procesos para todos los nodos paralelamente.

if __name__ == "__main__":
    main()