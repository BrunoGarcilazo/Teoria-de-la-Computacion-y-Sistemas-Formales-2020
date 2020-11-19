# TAREAS 1 - Conjunto de Tareas utilizadas para evaluar Alg.1 y Alg.2

tareas1 = [(1, 4), (3, 5), (0, 6), (5, 7),(3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]

# FIN TAREAS 1

# TAREAS 2 - CLASE "tarea" con sus atributos y luego las TAREAS usadas para evaluar Alg.3 y Alg.4

class tarea:
    def __init__(self,id,prioridad,duracion,horaInicio,horaFin,tipo,desc):
        self.id = id
        if prioridad > 5 or prioridad < 1:
            self.prioridad = 5
        else:
            self.prioridad = prioridad
        self.duracion = duracion
        self.horaInicio = horaInicio
        self.horaFin = horaFin
        self.tipo = tipo
        self.desc = desc

    def toString(self):
        print(self.tipo) # +

tareas = []
dia = []
for i in range(0,14,1):
    dia.append(-1)


p3 = tarea(3,   1,1,-1,-1,"Personal","pagar el alquiler")
p4 = tarea(4,   1,6,10,16,"Laboral","trabajar")
p2 = tarea(2,   2,2,-1,-1,"Personal","pagar cuentas pendientes")
p7 = tarea(7,   2,2,-1,-1,"Personal","estudiar")
p5 = tarea(5,   3,1,-1,-1,"Personal","sacar el perro")
p6 = tarea(6,   3,2,20,22,"Personal","partido de Uruguay")
p1 = tarea(1,   3,1,-1,-1,"Personal","salir a correr")
p8 = tarea(8,   4,1,-1,-1,"Personal","ir al supermercado")
p9 = tarea(9,   4,2,-1,-1,"Personal","arreglar la bicicleta")
p10 = tarea(10, 4,1,-1,-1,"Personal","comprar ropa")
p11 = tarea(11, 4,1,-1,-1,"Personal","comprar mueble")

tareas.append(p3)
tareas.append(p4)
tareas.append(p2)
tareas.append(p7)
tareas.append(p5)
tareas.append(p6)
tareas.append(p1)
tareas.append(p8)
tareas.append(p9)
tareas.append(p10)
tareas.append(p11)

#FIN TAREAS 2

# ALGORITMO 1 - Greedy (Alg.1)
print("ALGORITMO 1 - Greedy (Alg.1)")
def printMaxActivities(s , f ):
    n = len(f)
 
    i = 0
    print (i)
 
    for j in range(n):
        if s[j] >= f[i]:
            print (j)
            i = j
 
s = [1,3,0,5,3,5,6,8,8,2,12,3,2]
f = [2,5,6,7,8,9,10,11,12,13,14,6,4]
 
printMaxActivities(s , f)
print("FIN ALGORITMO 1 (Alg.1)" + "\n")
# FIN ALGORITMO 1 (Alg.1)


# ALGORITMO 2 - Dinamico (Alg.2)
print("ALGORITMO 2 - Dinamico (Alg.2)")
def findNonConflictingJobs(jobs):
 
    # sort the jobs according to increasing order of their start time
    jobs.sort(key=lambda x: x[0])
 
    # L[i] stores the maximum non-conflicting jobs that ends at i'th job
    L = [[] for _ in range(len(jobs))]
 
    for i in range(len(jobs)):
        # consider each j less than i
        for j in range(i):
            # L[i] = max(L[j]) where jobs[j].finish is less than jobs[i].start
            start, finish = (jobs[i][0], jobs[j][1])
            if finish < start and len(L[i]) < len(L[j]):
                L[i] = L[j].copy()
 
        # L[i] ends at i'th job
        L[i].append(jobs[i])
 
    # find the List having maximum size
    max = []
    for pair in L:
        if len(max) < len(pair):
            max = pair
 
    print(max)
 
if __name__ == '__main__':
 
    # Each pair stores the start and the finish time of a job
    jobs = [(1, 4), (3, 5), (0, 6), (5, 7),
            (3, 8), (5, 9), (6, 10), (8, 11),
            (8, 12), (2, 13), (12, 14)]
 
    findNonConflictingJobs(jobs)
print("FIN ALGORITMO 2 (Alg.2)" + "\n")
# FIN ALGORITMO 2 (Alg.2)



    
#ALGORITMO 3 (Alg.3)
print("ALGORITMO 3 (Alg.3)")
def organizarDia(tareas,dia):
    for i in range(0,len(tareas)-1,1):
        tareaX = tareas[i]       
        if(tareaX.prioridad == 1 and tareaX.horaInicio != -1 and tareaX.horaFin != -1): #No puedo ignorar esta tarea
            asignarTareaFija(tareaX,dia)
            continue
        else:
            result = obtenerTiempoLibre(tareaX.duracion,dia)
            if(result != -1):
                asignarTareaDuracion(tareaX,dia,result)

    return dia

def asignarTareaFija(tarea,dia):    #Asigna una tarea en el dia cuando esta tarea tiene un horario fijo.
    horaInicio = tarea.horaInicio - 8
    horaFin    = tarea.horaFin - 8
    for i in range(horaInicio,horaFin,1):
        dia[i] = tarea.id

def asignarTareaDuracion(tarea,dia,indiceInicio):
    for i in range(indiceInicio,indiceInicio+tarea.duracion,1):
        dia[i] = tarea.id

def obtenerTiempoLibre(horas,dia): #Busca tiempo libre de X horas y devuelve el indice del dia donde empieza ese tiempo libre, sino devuelve -1
    aux = 0
    for i in range(0,14,1):
        if(dia[i]==-1):
            aux+=1
            if(aux==horas):
                return i - (horas-1)
        else:
            aux = 0 
    return -1

#Imprime la planificacion del dia.
def printDia(tareas,dia):
    for i in range(0,14,1):
        print(getDescTarea(dia[i],tareas))

def getDescTarea(id,tareas):
    for i in range(0,len(tareas)-1,1):
        if tareas[i].id == id:
            return tareas[i].desc
    return "null"

organizarDia(tareas,dia)
printDia(tareas,dia)
print("FIN ALGORITMO 3 (Alg.3)")
# FIN ALGORITMO 3 (Alg.3)
