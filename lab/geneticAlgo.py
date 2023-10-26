
import random
population_size = 10
target_value = 255
max_generation = 100
generation = 0
def fintness_Check(x):
    return abs(x**2+45 - target_value)

def initialize_population():
    temp_population = []
    for i in range(population_size):
        temp_population.append(random.uniform(0,50))
    return temp_population

population = initialize_population()

while generation < max_generation:
    fitness_score = []
    for num in population:
        fitness_score.append((fintness_Check(num),num))
    
    fitness_score.sort()
    if(fitness_score[0][0] <= 10):
        print(f"solution found in generation: {generation} and number is: {fitness_score[0][1]}")
        break

    fitness_score = fitness_score[:5]
    off_spring = []
    for i in range(100):
        off_spring.append(fitness_score[random.randrange(0,5)][1] * random.uniform(0.97,1.3))
    population = off_spring[:population_size]
    generation = generation+1