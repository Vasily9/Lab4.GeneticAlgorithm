import readFile 
import pyeasyga


def fitness(ind, data): #функция приспособленности
    w = 0
    v = 0
    value = 0
    for (selected, item) in zip(ind, data):
        if selected:
            w += item[0]
            v += item[1]
            value += item[2]
    if w > readFile.weight or v > readFile.volume: #обнуляем значение, если выходит за границу
        value = 0
    return value

def start():
    file=readFile.items #берем данные из файла
    ga = pyeasyga.GeneticAlgorithm(file) #используем библиотеку генетического алгоритма
    ga.population_size = 200    #повышаем популяцию до 200
    ga.fitness_function = fitness 
    ga.run()  #запускаем генетический алгоритм
    return ga.best_individual()  #возвращаем резудьтат 
	
readFile.read()
res=start()
print(res[0],res[1])
