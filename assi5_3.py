import random
import math
random_number = [0.655, 0.254, 0.432]
def evaluate_solution(solution):
    clauses = [((not solution[0]) or solution[3]),
                (solution[2] or solution[1]),
                ((not solution[2]) or (not solution[3])),
                ((not solution[3]) or (not solution[1])),
                ((not solution[0]) or (not solution[3]))]
    return sum(clauses)

def movegen(solution):
    var_index = random.randint(0, len(solution)-1)
    solution_copy = solution[:]
    solution_copy[var_index] = not solution_copy[var_index]
    return solution_copy

def accept_bad_move(delta, temperature, i):
    
    probability = 1/(1 + math.exp(-delta / temperature))
    return random_number[i] < probability

def simulated_annealing():
    T=500
    cooling_factor=50
    current_solution=[True,True,True,True]
    current_energy=evaluate_solution(current_solution)
    best_solution=current_solution[:]
    best_energy=current_energy
    i = 0
    while T>0:
        if i == 3:
            break
        new_solution=movegen(current_solution)
        new_energy=evaluate_solution(new_solution)
        delta=new_energy-current_energy
        if delta>0 or accept_bad_move(delta, T, i):
            current_solution=new_solution[:]
            current_energy=new_energy
            if new_energy>best_energy:
                best_solution=new_solution[:]
                best_energy=new_energy
        i = i+1
        print(f"Iteration : {i}")
        print(f"Current Candidate : f{current_solution}")
        print(f"Curr Score : {current_energy}")
        print(f"Best Candidate : {best_solution}")
        print(f"Best Score : {best_energy}")
        print()
        T-=cooling_factor
    return best_solution


best_solution=simulated_annealing()
print("Best Solution:",best_solution)
print("Clauses satisfied:",evaluate_solution(best_solution))
