import random

# Define the parameters
max_generation = 100  # Maximum number of generations
population_size = 10  # Size of the population
mutation_rate = 0.1  # Probability of mutation

# Define your fitness function
def fitness_function(instance, target_output):
    # Calculate the error (difference from the target output)
    error = abs(int(instance, 2) - target_output)
    return error

# Generate initial population
def generate_initial_population(population_size):
    return ['{0:08b}'.format(random.randint(0, 255)) for _ in range(population_size)]

# Crossover function (single-point crossover)
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Mutation function (bit flip mutation)
def mutate(child):
    mutated_child = list(child)
    for i in range(len(mutated_child)):
        if random.random() < mutation_rate:
            mutated_child[i] = '1' if mutated_child[i] == '0' else '0'
    return ''.join(mutated_child)

# Main genetic algorithm loop
def genetic_algorithm(target_output):
    population = generate_initial_population(population_size)
    for generation in range(max_generation):
        # Calculate fitness scores
        fitness_scores = [fitness_function(instance, target_output) for instance in population]

        # Check for solution
        if 0 in fitness_scores:
            index = fitness_scores.index(0)
            solution = population[index]
            print(f"Solution found in generation {generation}: {solution}")
            break

        # Sort population based on fitness scores
        sorted_population = [x for _, x in sorted(zip(fitness_scores, population))]

        # Select parents for crossover (top 50% of the population)
        parents = sorted_population[:population_size // 2]

        # Create new population through crossover and mutation
        new_population = []
        while len(new_population) < population_size:
            parent1, parent2 = random.choice(parents), random.choice(parents)
            child1, child2 = crossover(parent1, parent2)
            child1 = mutate(child1)
            child2 = mutate(child2)
            new_population.extend([child1, child2])

        # Update the population
        population = new_population

# Example usage
target_output = 255  # Change this to your target output value
genetic_algorithm(target_output)