import timeit

start = timeit.default_timer()


grafo = {'A':[('B',2),('D',6)],
         'B':[('A',2),('J',1),('C',2)],
         'C':[('B',2),('I',3),('F',1)],
         'D':[('A',6),('I',4),('M',3)],
         'J':[('B',1),('I',2)],
         'I':[('J',2),('C',3),('D',4),('H',2),('K',7)],
         'F':[('C',1),('G',2),('K',1)],
         'K':[('F',1),('G',4),('I',7)],
         'M':[('D',3),('N',5),('H',3)],
         'H':[('G',2),('I',2),('M',3),('N',3)],
         'G':[('F',2),('K',4),('L',2),('H',2)],
         'L':[('G',2),('N',1)],
         'N':[('H',3),('L',1),('M',5)]
           }

def UniformCostSearch(grafo,inicial,final):
    
  nodosExpandir = []   # Arreglo de nodos que serviran para cada iteracion
  nodosVisitados = [] # Arreglo de nodos ya visitados y con su costo de llegada
  colaPrioridad = [] # Lista de caminos ejecutados en una iteracion

  nodosExpandir.append(inicial) 
  nodosVisitados.append([inicial, 0])
  x = 0
   
    # I es el nodo en donde estamos
    # J es uno de los caminos del nodo I 

  while True:
    # Aqui se hace cada iteracion para visualizar
    colaPrioridad.append([])                  # Creamos cada sublista de cada iteracion
    menorCosto = 100000000
    for I in nodosExpandir:                   # Recorrer los nodos a expandir 
      for Y in nodosVisitados:                # Aqui conseguimos costo minimo en lo que se llega al nodo
            if Y[0] == I[0]:
              costoNodo = Y[1]

      for J in grafo[I]:                      # Recorremos todos los camino de cada nodo
        visitado = 0
        for W in nodosVisitados:              # Buscamos si el nodo  lo hemos visitado
          if J[0] == W[0]:
            visitado = 1

        if visitado == 0:                    # Si el nodo no ha sido visitado
          if costoNodo + J[1] <= menorCosto:  # evaluamos el camino de menor costo
            menorCosto = costoNodo + J[1]
            nodoVisitado = J[0]
          colaPrioridad[x].append([I,J[0],costoNodo + J[1]])
    x = x + 1                       # Vamos al siguiente camino de esta iteracion      

    nodosVisitados.append([nodoVisitado,menorCosto])      # agregamos al nodo de menor costo que visitamos
    nodosExpandir.append(nodoVisitado)                    # ese nodo lo expandiremos
    if nodoVisitado == final:  # si llegamos al nodo final nos salimos del bucle
      break                     
      
      # Revisamos los nodos a expandir y checamos si esos nodos pueden seguir expandiendose
    for K in nodosExpandir:                 
      nodoTerminado = 0
      for Z in grafo[K]:                   # Checamos todos los caminos de cada nodo a expandir
        for E in nodosVisitados:           # recorre todos los nodos visitados
          if Z[0] == E[0]:
            nodoTerminado = nodoTerminado + 1   # Contabiliza 
      if nodoTerminado  == len(grafo[K]):
        nodosExpandir.remove(K)
    # Aqui se creara la cola de prioridad final      
  colaComparacion = []
  for H in range(x): # Queremos saber la camino menor de cada iteracion
    menorIteracion = 1000000000  
    for T in range(0, len(colaPrioridad[H])):  # Aqui vamos pasando por los caminos de la iteracion x           
      if colaPrioridad[H][T][2] <= menorIteracion: # evaluamos cada camino para ver cual es el de menor coste
        nodoIni = colaPrioridad[H][T][0] 
        nodoFin = colaPrioridad[H][T][1] 
        menorIteracion = colaPrioridad[H][T][2]
    colaComparacion.append([nodoIni,nodoFin,menorIteracion])  # creamos una nueva lista con los caminos mas cortos de cada iteracion  

  caminoSeguir = []  # aqui aparecera el camino a seguir
  caminoSeguir.append(nodoFin) 
  costoFinal = menorIteracion

  nodoCamino = x - 1
  nodoComparacion = nodoCamino - 1
  while nodoCamino >= 0 : 
    if colaComparacion[nodoCamino][0] == colaComparacion[nodoComparacion][1]:
      caminoSeguir.append(colaComparacion[nodoComparacion][1])
      nodoCamino = nodoComparacion
      nodoComparacion = nodoCamino - 1
    else:
      nodoComparacion = nodoComparacion - 1 
    if nodoComparacion < 0:
      break
  caminoSeguir.append(inicial)  
  caminoSeguir.reverse()                      # Volteamos el camino
  print(f'El camino es {caminoSeguir} con un coste de {costoFinal} ') # Imprimimos el camino y su coste   

if __name__ == '__main__':
    
    inicial = 'A' 
    final = 'N'

    UniformCostSearch(grafo,inicial,final)
    end = timeit.default_timer()
    print("Terminado en --- %s segundos ---" % (end - start))
    
     
             
            
            

