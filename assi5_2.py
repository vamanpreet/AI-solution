# 0/1 Knapsack

import random
MAX_CAPACITY=9
POPULATION_SIZE=4
ITERATIONS=4
MUTATION_BITS=[2,0,3,1]
items=[
    {"name":"Mirror","weight":2,"value":3},
    {"name":"Silver Nugget","weight":3,"value":5},
    {"name":"Painting","weight":4,"value":7},
    {"name":"Vase","weight":5,"value":9},
]



def calculate_fitness(chromosome):
    total_weight=sum(chromosome[i]*items[i]["weight"] for i in range(len(items)))
    total_value=sum(chromosome[i]*items[i]["value"] for i in range(len(items)))
    if total_weight>MAX_CAPACITY:
        total_value=0
    return total_value

def selection(population):
    sorted_population=sorted(population,key=calculate_fitness, reverse=True)
    return sorted_population

def crossover(parent1, parent2):
    crossover_point=len(parent1)//2
    child=parent1[:crossover_point]+parent2[crossover_point:]
    return child

def mutation(chromosome):
    mutated_choromosome=chromosome.copy()
    for bit in MUTATION_BITS:
        mutated_choromosome[bit]=1-mutated_choromosome[bit]
    return mutated_choromosome

population=[[1,1,1,1],[1,0,0,0],[1,0,1,0],[1,0,0,1]]

for iteration in range(ITERATIONS):
    print(f"Iteration {iteration+1}:")
    print("Population: ",population)
    selected=selection(population)
    print(selected)
    print("Selected: ",selected[:2])
    offspring=crossover(selected[2],selected[3])
    print("Offspring: ",offspring)
    mutated_offspring=mutation(offspring)
    print("Mutated Offspring: ",mutated_offspring)
    index = population.index(selected[3])
    population[index]=mutated_offspring
    print()
best_chromosome=max(population, key = calculate_fitness)
print("Final Best Chromosome: ",best_chromosome)
selected_items=[items[i]["name"] for i in range(len(items)) if best_chromosome[i]==1]
print(f"Selected Items : {selected_items}")
print("Final Fitness Value: ", calculate_fitness(best_chromosome))
    