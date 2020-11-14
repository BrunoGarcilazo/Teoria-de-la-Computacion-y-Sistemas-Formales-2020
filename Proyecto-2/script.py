# Script para solcucionar el "Activity Selection Problem" del Problema 1 - Proyecto 2

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
    
# Criterios a seguir:
    # Ordenar tareas por Prioridad (mayor prioridad primero)
    # Las de Prioridad 1 y horario fijo, agendarlas para el dia.
    # Agendar las restantes de prioridad 1 sin horario fijo.
    # Agendar posibles restantes de otras prioridades donde se pueda (tiempos libres)

def organizarDia(tareas,dia): #WIP
    for i in range(0,len(tareas)-1,1):
        print(dia)
        tareaX = tareas[i]
        print(tareaX.duracion)
        
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