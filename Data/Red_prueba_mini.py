import math

############################################################################



global Escala
global edges
global nodes
global coord
global Dismax
# Red de ejemplo para desarrollo
edges = {('A', 'B'), ('B', 'C'), ('C', 'D')}
nodes = {'A', 'B', 'C', 'D'}
coord = {'A': (0, 0), 'B': (1, 0), 'C': (3, 0), 'D': (6, 0)}


#Endurance
Dismax = 2500

def Calcula_escala(Nodo1, Nodo2, Distancia_real):
    global coord
    escala = 1

    dista_no_escala = math.sqrt((coord[Nodo1][0] - coord[Nodo2][0]) ** 2 + (coord[Nodo1][1] - coord[Nodo2][1]) ** 2)
    escala = Distancia_real / dista_no_escala

    return escala
# Real distance of Segment to compute scale of the network
Escala = Calcula_escala('A', 'B', 2000)  # Escala para la red pequeña de prueba