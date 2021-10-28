import sys #permite usar la funcion maxsize para representar un numero enorme.
import concurrent.futures 
import numpy as np
import time

#definimos como fuente el nodo incial del grafo
#los otros nodos los llamare vertices
#basado en: https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/

class Graph():
    def __init__(self,vertices): #inicializando con los vertices
        self.V=vertices
        self.graph = [[0 for columnas in range(vertices)] 
        for lineas in range(vertices)] #queremos una matriz cuadrada

    ''' def printSolucion(self,dist,src): #dist es la lista de distancias
        print("\tDistancia a los vertices desde el nodo {}".format(src))
        for node in range(self.V):
            if(node != src):
                print("\trouter" ,node, "--> ", dist[node]) '''
    
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

        #self.printSolucion(dist,src) #imprime las distancias
        return dist


def main():
    
    print("Grafo de baja complejidad:\n")
    nodos_LC = 8
    Low_complexity = Graph(nodos_LC)
    Low_complexity.graph = np.loadtxt("Baja_complejidad.txt",skiprows=0).astype(int)
    nodes = [i for i in range(nodos_LC)] 
    start_l = time.time()
    with concurrent.futures.ProcessPoolExecutor() as executor_LC: #crea un ejecutor de multi-procesos para el grafo de baja complejidad
        results = executor_LC.map(Low_complexity.dijkstra,nodes) #ejecuta dijkstra en varios procesos para todos los nodos paralelamente.
        #la funcion .map permite sacar en el output en el Visual Studio de forma ordenada
        #sale desordenado en el terminal.
    fin_l=time.time()
    for idx,result in enumerate(results):
        #print(f'{idx}|{result}')
        print(f'Distancia a los vertices desde el nodo {idx}:')
        for id,dist in enumerate(result):
            if(dist!=0):
                print(f"\trouter {id} --> {dist}")
        print("\n")
    
    print(f'Time in low complexity = {fin_l-start_l}')
    print("---------------------------------------------------\n")
    print("Grafo de alta complejidad:\n")
    
    nodos_HC = 11
    High_complexity = Graph(nodos_HC)
    High_complexity.graph = np.loadtxt("Alta_complejidad.txt",skiprows=0).astype(int)
    nodes = [i for i in range(nodos_HC)] 
    start_h=time.time()
    with concurrent.futures.ProcessPoolExecutor() as executor_HC: #crea un ejecutor de multi-procesos para el grafo de alta complejidad
        results = executor_HC.map(High_complexity.dijkstra,nodes) #ejecuta dijkstra en varios procesos para todos los nodos paralelamente.
    fin_h = time.time()
    for idx,result in enumerate(results):
            #print(f'{idx}|{result}')
        print(f'Distancia a los vertices desde el nodo {idx}:')
        for id,dist in enumerate(result):
            if(dist!=0):
                print(f"\trouter {id} --> {dist}")
        print("\n")
    
    print(f'Time in high complexity = {fin_h-start_h}')
    print(f'Total time {(fin_h-start_h)+(fin_l-start_l)}')
if __name__ == "__main__":
    main()