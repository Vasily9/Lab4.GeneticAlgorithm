weight=0 #вес 
volume=0 #объем
items=[] #предметы

def read(): #считываем данные из файла
    file = open('22.txt', 'r')
    str= [line.strip() for line in file]
    file.close()
    global weight
    weight=int(str[0].split(' ')[0])
    global volume
    volume=int(str[0].split(' ')[1])
    str.remove(str[0])
    for i in str:
        global items
        item=i.split(' ')
        items.append((int(item[0]),float(item[1]),int(item[2])))
