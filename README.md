# Drone Monitoring
Data for "Monitoring network infrastructures with drones: 
Application to the railway commuter network of Madrid" submitted to *Applied Mathematical Modelling*
--------------------------------------------------------------------------------------------------------------------------------------------------------------
This repository contains the data used for the article "**Monitoring network infrastructures with drones: Application to the railway commuter network of Madrid**". 
by David Canca, José Miguel León Blanco, José Luis Andrade Pineda, Pedro Luis González-R and Marcos Calle

The description of the network is included as a Python File named **"Cercanias_madrid.py"** containing the network stations and the links connecting these stations  for the Commuter Railway Network of Madrid. 

The Python File also contains the scale of the network, so that it is possible to obtain the coordinates of nodes and the length of segments.


As an example, the file **"Cercanias_madrid.py"** contains:
A dictionary of edges (Railway section between stations)
A dictionary of nodes (stations) 
A dictionary with the coordinates of nodes

````python
import math

#####################  CERCANIAS MADRID
edges={
('Aeropuerto','Valdebebas'),
('Alcalá Universidad','Alcalá de Henares'),
('Alcalá de Henares','La Garena'),
('Alcobendas','Valdelasfuentes'),
('Alcorcón','San José Valderas'),
('Alpedrete','Los Negrales'),
('Aluche','Laguna'),
('Aravaca','Principe Pío'),
('Atocha','Méndez Álvaro 2'),
('Atocha','Méndez Álvaro'),
('Azuqueca','Meco'),
('Cantoblanco','Fuencarral'),
('Cercedilla','Los Molinos'),
('Chamartín','Nuevos Ministerios'),
('Cien Pozuelos','Aranjuez'),
('Collado Mediano','Alpedrete'),
('Colmenar Viejo','Tres Cantos'),
('Coslada','Vicálvaro'),
('Cuatro Vientos','Las Águilas'),
('Delicias','Pirámides'),
('Doce de Octubre','Méndez Álvaro'),
('El Barrial','Pozuelo'),
('El Casar','Getafe Industrial'),
('El Escorial','Zarzalejo'),
('El Goloso','Cantoblanco'),`
...
}
````
````python
nodes={
'Aeropuerto',
'Alcalá Universidad',
'Alcalá de Henares',
'Alcobendas',
'Alcorcón',
'Alpedrete',
'Aluche',
'Aranjuez',
'Aravaca',
'Atocha',
'Azuqueca',
'Cantoblanco',
'Cercedilla',
'Chamartín',
'Cien Pozuelos',
'Collado Mediano',
'Colmenar Viejo',
'Coslada',
'Cuatro Vientos',
'Delicias',
'Doce de Octubre',
'El Barrial',
'El Casar',
'El Escorial',
'El Goloso',
'El Pozo',
...
}
````
````python
coord={
'Aeropuerto':(123.09,100.68),
'Alcalá Universidad':(166.43,104.69),
'Alcalá de Henares':(159.82,99.66),
'Alcobendas':(117.54,112.58),
'Alcorcón':(82.55,68.6),
'Alpedrete':(49.2,136.58),
'Aluche':(94.20,76.33),
'Aranjuez':(118.92,0),
'Aravaca':(95.33,85.45),
'Atocha':(107.17,80.87),
'Azuqueca':(176.75,115.27),
'Cantoblanco':(104.84,112.32),
'Cercedilla':(45,154.09),
'Chamartín':(107.29,95.41),
'Cien Pozuelos':(120.3,28.07),
'Collado Mediano':(49.41,143.74),
'Colmenar Viejo':(92.34,133.56),
'Coslada':(131.79,81.29),
'Cuatro Vientos':(90.14,74.26),
'Delicias':(105.53,79.24),
'Doce de Octubre':(103.73,76.64),
'El Barrial':(90.83,88.36),
'El Casar':(102.81,62.25),
'El Escorial':(33.73,122.1),
'El Goloso':(100.87,114.96),
'El Pozo':(117.22,69.5),
'El Soto':(72.77,66.32),
'Embajadores':(104.06,81.22),
'Entrevías':(115.1,69.5),
'Fuencarral':(108,102.8),
'Fuenlabrada':(87.03,53.08),
...
}
````
````python
# Endurance
Dismax = 10000

# Function to scale network to real measures
def Calcula_escala(Nodo1, Nodo2, Distancia_real):
    global coord
    escala = 1

    dista_no_escala = math.sqrt((coord[Nodo1][0] - coord[Nodo2][0]) ** 2 + (coord[Nodo1][1] - coord[Nodo2][1]) ** 2)
    escala = Distancia_real / dista_no_escala

    return escala

# Reference segment between stations to calculate the scale
Escala=Calcula_escala('Valdemoro','Pinto',5920)
````


A second little network used to develop the code is included in the file "**"Red_prueba_mini.py"**".


## Reuslts of the research.

The results are stored in the folder "Results".

Inside the folder there are two sub-folders concerning the results of the base experiment and the results of the sensitivity analysis experiments.

The folder "Sensitivity Analysis" contains 3 subfolders corresponding to 3 different daily workin shift duration **$\mathcal{D}=\lbrace 10,9,8 \rbrace$** hours. Every subfolder is divided in 4 new folders, depending on the drone endurance **$\mathcal{E}=\lbrace 12000, 10000, 8000, 6000 \rbrace$** meters. Inside each folder there are 3 new subfolders corresponding to the three values of the charge rate, **$RC=\lbrace 1.8, 1.9, 2.0 \rbrace$** time to charge/ time employed for trips.

Inside each of these last forlders there are six graphs numbered form 00 to 05:

*00 -> Base network of the Madrid Commuter railway Network*

*01 -> Network coverage with paths*

*02 -> Network Coverage with Segments*

*03 -> Circular graph of Segments to solve the double direction VRP model*

*04 -> Solution of the VRP double direction model over the circular graph of Segments*

*05 -> Final assignment of drones to segments*



