import Queue

print("Essa e uma Tarefa de Bruno Hryniewicz e Nickolas Gomes da materia de Sistemas Operacionais")
x = 0
x = int(input())
entrada = []
temp = []
prio = []
entrada = list(map(int,raw_input().split()))
temp = list(map(int,raw_input().split()))
prio = list(map(int,raw_input().split()))

class Tarefa:

    def __init__(self, entrada, temp, prio):
        self.entrada = entrada
        self.temp = temp
        self.prio = prio
        self.prioOri = prio
        self.timeExec = 0
        self.done = False
        self.doneAt = 0
    def doWork(self, timer):
        self.timeExec += 1
        self.doneAt = timer
        if(self.timeExec == self.temp):
            self.done = True
    def printT(self):
        print("Entrada: %d, Temp: %d, Prio: %d, TimeExec: %d, Done: "+str( self.done), self.entrada,
        self.temp, self.prio, self.timeExec, self.doneAt, self.doneAt - self.temp)


def loadTarefas(tarefas):
    for i in range(x):
        tarefas.append(Tarefa(entrada[i], temp[i], prio[i]))

def calcTimer(x, tarefas, name):
    tt = 0.0
    tw = 0.0
    for tarefa in tarefas:
        tt += tarefa.doneAt - tarefa.entrada
        tw += tarefa.doneAt - tarefa.entrada - tarefa.temp
    print( name + " tt = " + str(tt/x))
    print( name + " tw = " + str(tw/x))

def FCFS(x):
    trocas = -1
    tarefas=[]
    loadTarefas(tarefas)
    timer = 0
    fila = Queue.Queue(x)
    workingIn = Tarefa(0,0,0)
    workingIn.done = True
    while(True):
        for tarefa in tarefas:
            if(tarefa.entrada == timer):
                fila.put(tarefa)
        if (workingIn.done):            
            if(fila.empty()):
                break
            trocas += 1
            workingIn = fila.get()
        timer += 1
        workingIn.doWork(timer)


        
    print("FCFS trocas de contexto = "+str( trocas))
    calcTimer(x, tarefas, "FCFS")
    print("")
    

FCFS(x)

def RR (x,  frame):
    trocas = -1
    tarefas=[]
    loadTarefas(tarefas)
    timer = 0
    fila = Queue.Queue(x)
    workingIn = Tarefa(0,0,0)
    workingIn.done = True
    onWork = 0

    while(True):
        for tarefa in tarefas:
            if(tarefa.entrada == timer):
                fila.put(tarefa)
        if (workingIn.done):            
            if(fila.empty()):
                break
            trocas += 1
            workingIn = fila.get()
            onWork = 0
        timer += 1
        workingIn.doWork(timer)
        onWork += 1

        if (onWork == frame):
            if(workingIn.done):
                continue
            fila.put(workingIn)
            trocas += 1
            workingIn = fila.get()
            onWork = 0

    print("RR trocas de contexto :" + str(trocas))
    calcTimer(x, tarefas, "RR")
    print("")

RR(x, 2)


def SJF(x):
    trocas = -1
    tarefas=[]
    loadTarefas(tarefas)
    timer = 0
    fila = Queue.PriorityQueue(x)
    workingIn = Tarefa(0,0,0)
    workingIn.done = True
    while(True):
        for tarefa in tarefas:
            if(tarefa.entrada == timer):
                fila.put((tarefa.temp, tarefa))
        if (workingIn.done):            
            if(fila.empty()):
                break
            trocas += 1
            workingIn = fila.get()[1]
        timer += 1
        workingIn.doWork(timer)


        
    print("SJF trocas de contexto = "+str( trocas))
    calcTimer(x, tarefas, "SJF")
    print("")

SJF(x)

def SRTF (x):
    trocas = -1
    tarefas=[]
    loadTarefas(tarefas)
    timer = 0
    fila = Queue.PriorityQueue(x)
    workingIn = Tarefa(0,0,0)
    workingIn.done = True
    old = workingIn

    while(True):
        for tarefa in tarefas:
            if(tarefa.entrada == timer):
                fila.put((tarefa.temp,tarefa))
        if (workingIn.done):            
            if(fila.empty()):
                break
            trocas += 1

            workingIn = fila.get()[1]

        elif(not fila.empty()):
                
            aux = fila.get()[1]
            if (workingIn.temp - workingIn.timeExec <= aux.temp - aux.timeExec):

                fila.put((aux.temp - aux.timeExec, aux))
            else:
                fila.put((workingIn.temp - workingIn.timeExec, workingIn))

                workingIn = aux
                trocas += 1

        timer += 1
        workingIn.doWork(timer)






    print("SRTF trocas de contexto :" + str(trocas))
    calcTimer(x, tarefas, "SRTF")
    print("")

SRTF(x)

def PRIOc(x):
    trocas = -1
    tarefas=[]
    loadTarefas(tarefas)
    timer = 0
    fila = Queue.PriorityQueue(x)
    workingIn = Tarefa(0,0,0)
    workingIn.done = True
    while(True):
        for tarefa in tarefas:
            if(tarefa.entrada == timer):
                fila.put((-tarefa.prio, tarefa))
        if (workingIn.done):            
            if(fila.empty()):
                break    
            trocas += 1
            workingIn = fila.get()[1]
        timer += 1
        workingIn.doWork(timer)
        
    print("PRIOC trocas de contexto = "+str( trocas))
    calcTimer(x, tarefas, "PRIOc")
    print("")

PRIOc(x)

    
def PRIOp (x):
    trocas = -1
    tarefas=[]
    loadTarefas(tarefas)
    timer = 0
    fila = Queue.PriorityQueue(x)
    workingIn = Tarefa(0,0,0)
    workingIn.done = True

    while(True):
        for tarefa in tarefas:
            if(tarefa.entrada == timer):
                fila.put((-tarefa.prio,tarefa))
        if (workingIn.done):            
            if(fila.empty()):
                break
            trocas += 1
            workingIn = fila.get()[1]
        elif(not fila.empty()):
            aux  = fila.get()[1]
            if (aux.prio > workingIn.prio):
                fila.put((-workingIn.prio,workingIn))
                trocas += 1
                workingIn = aux
            else: 
                fila.put((-aux.prio, aux))
        timer += 1

        workingIn.doWork(timer)


    print("PRIOp trocas de contexto =" + str(trocas))
    calcTimer(x, tarefas, "PRIOp")
    print("")
PRIOp(x)            

def atualizaFila(fila, timer):
    vetAux = []
    while (not fila.empty()):
        vetAux.append(fila.get())
    for tarefa in vetAux:
        tarefa = tarefa[1]
        tarefa.prio = tarefa.prioOri + timer - tarefa.doneAt
        fila.put((-(tarefa.prio), tarefa))


def PRIOd (x):
    trocas = -1
    lenFila = 0
    tarefas=[]
    loadTarefas(tarefas)
    timer = 0
    fila = Queue.PriorityQueue(x)
    workingIn = Tarefa(0,0,0)
    workingIn.done = True

    while(True):
        # workingIn.printT()
        # print(timer)
        for tarefa in tarefas:
            if(tarefa.entrada == timer):
                tarefa.doneAt = timer
                fila.put((-(tarefa.prio),tarefa))
        if (workingIn.done):            
            if(fila.empty()):
                break
            trocas += 1
            workingIn = fila.get()[1]
            workingIn.prio = workingIn.prioOri
            lenFila = fila.qsize()
        elif(not fila.empty()):
            if (lenFila < fila.qsize()):
                aux = fila.get()[1]
                if (workingIn.prio < aux.prio ):
                    fila.put((-(workingIn.prio ),workingIn))
                    trocas +=1
                    workingIn = aux
                else:
                    fila.put((-(aux.prio ), aux))
                lenFila = fila.qsize()

        timer += 1
        workingIn.doWork(timer)
        atualizaFila(fila, timer)
        # workingIn.printT()
        # print(trocas)


    print("PRIOd trocas de contexto =" + str(trocas))
    calcTimer(x, tarefas, "PRIOd")
    print("")

PRIOd(x)
            
    
        

