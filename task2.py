import readFile
import random

def topPop(bag, pop, percent=100): #выбор наиболее приспособленных особей
    percent = percent % 100
    sort = {}
    oldpop = sorted(sort, key=sort.__getitem__)
    oldpop.reverse()
    top = int(len(oldpop)*percent/100)
    if top % 2 == 1:
        top -= 1
    h = []
    t = []
    for i in range(0, top):
            h.append(pop[oldpop[i]])
    for i in range(top, len(oldpop)):
            t.append(pop[oldpop[i]])
    return {"h" : h, "t" : t}

def fitness(): #приспособленность
    for i in range(0,len(oldpop)):
        val = 0
        vol=0
        w=0
        for j in range(0,len(oldpop[i][0])):
            if oldpop[i][0][j]==1:
                val+=things[j][2]
                w+=things[j][0]
                vol+=things[j][1]
                if w>readFile.weight or vol>readFile.volume:
                    val=0
                    break
        oldpop[i].append([val])
		
def mutation(): #мутация путем инвентирования всех битов 1 особи
    ind = random.randint(0, len(oldpop)-1)				
    for x in range(0,len(oldpop[ind])-1):
        if oldpop[ind][x]==0 :
            oldpop[ind][x] = 1
        else:
            oldpop[ind][x] = 0		
		
def selection(): #отбор особей для скрещивания
    sum=0
    par=oldpop.copy()
    for k in range(0,len(oldpop)):
        sum+=oldpop[k][1][0]
    while len(par)>0:
        i = 0
        random.seed()
        r = random.randint(0, round(sum))
        csum=0
        while csum<r and i<len(par):
            csum+=par[i][1][0]
            i+=1
        sum-=par[i-1][1][0]
        m=par[i-1][0]
        par.remove(par[i-1])
        i=0
        random.seed()
        r = random.randint(0, round(sum))
        csum=0
        while csum<r and i<len(par):
            csum+=par[i][1][0]
            i+=1
        sum -= par[i - 1][1][0]
        f = par[i - 1][0]
        par.remove(par[i - 1])
        cr(m, f)
		

def startPop(): #запуск популяции
    it=sorted(readFile.items,key=lambda x: x[2])
    global things
    things=it[::-1]
    for i in range (0,pcount):
        random.seed()
        ind=random.randint( 0, len(things))
        cw=0
        cv=0
        oldpop.append([])
        oldpop[i].append([])
        for j in range(0,ind):
            oldpop[i][0].append(0)
        for j in range(ind,len(things)):
            if cw+things[j][0]<readFile.weight and cv+things[j][1]<readFile.volume:
                oldpop[i][0].append(1)
                cw+=things[j][0]
                cv+=things[j][1]
            else:
                oldpop[i][0].append(0)
        for k in range(0,len(oldpop[i][0])):
            if oldpop[i][0][k]==0:
                if cw + things[k][0] < readFile.weight and cv + things[k][1] < readFile.volume:
                    oldpop[i][0][k]=1
                    cw += things[k][0]
                    cv += things[k][1]
            else:
                break

def selh(): #вспомогательная функция
    sum=0
    for p in oldpop:
        sum += p[1]
    sp = random.randint(0, sum)
    sum=0
    i=0
    while sum<sp:
        sum+=oldpop[i][1]
        i+=1
    item=oldpop[i-1]
    old.append(item)
    del oldpop[i-1]
    return item	  


def SelectPar():#скрещивание 2-х пар
    item1=Selection()
    item2 = Selection()
    child=Cross(item1[0],item2[0])
    for c in child:
        new.append([c,FitnessFunc(c)])

def Cross(x,y):#многоточечное скрещивание с 3мя точками  
    c1= []
    c2= []
    leng=len(y)
    d1=random.randint(0, leng//2)
    d2=random.randint(d1, leng-1)
    d3=random.randint(d2, leng-1)
    for i in range(0,d1):
        c1.append(x[i])
        c2.append(y[i])
    for i in range(d1,d2):
        c1.append(y[i])
        c2.append(x[i])
    for i in range(d2, d3):
        c1.append(x[i])
        c2.append(y[i])
    for i in range(d3,leng):
        c1.append(y[i])
        c2.append(x[i])
    return [c1,c2]	
       

def gF(child): 
    val=0
    vol = 0
    w = 0
    for j in range(0, len(child)):
        if child[j] == 1:
            val += things[j][2]
            w += things[j][0]
            vol += things[j][1]
            if w > readFile.weight or vol > readFile.volume:
                val = 0
                break
    return val	
	
def cr(x, y):
    child=[]
    for i in range(0,len(x)):
        random.seed()
        ind = random.random()
        if (ind<0.5):
            child.append(x[i])
        else:
            child.append(y[i])
    ch=[]
    ch.append(child)
    ch.append([gF(child)])
    newpop.append(ch)



def newPop(): #формирование новой популяции
    global oldpop
    spop=sorted(oldpop+newpop,key=lambda x: x[1])
    spop=spop[::-1]
    oldpop=spop[0:200]

def start(x): #объединяем функции
    global oldpop
    oldpop = []
    global newpop
    newpop = []
    global things
    things = []
    startPop()
    fitness()
    for k in range(0,x):
        selection()
        newPop()
    return oldpop[0]
		
oldpop=[]
newpop=[]
pcount=200
things=[]	
	
	
readFile.read()
res=start(100)
print(res[1],res[0])
