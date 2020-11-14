class tarea:
    def __init__(self,prioridad,duracion,horaInicio,horaFin,tipo):
        if prioridad > 5 or prioridad < 1:
            self.prioridad = 5
        else:
            self.prioridad = prioridad
        self.duracion = duracion
        self.horaInicio = horaInicio
        self.horaFin = horaFin
        self.tipo = tipo

    def toString(self):
        print(self.tipo)



p1 = tarea(1,30,18,22,"Personal")
p1.toString()

def printMaxActivities(s , f ):
    n = len(f)
 
    i = 0
    print (i),
 
    for j in range(n):
        if s[j] >= f[i]:
            print (j),
            i = j
