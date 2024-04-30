import sys

# Function to calculate the distance between two cities
def distance(city1, city2):
    distances = {
        (1, 2): 10, (1, 3): 15, (1, 4): 20,
        (2, 3): 35, (2, 4): 25, (3, 4): 40,
        (2, 1): 10, (3, 1): 15, (4, 1): 20,
        (3, 2): 35, (4, 2): 25, (4, 3): 40
    }
    return distances.get((city1, city2), sys.maxsize)

# Function to find the nearest neighbor of a city
def nearest_neighbor(current_city, unvisited_cities):
    nearest_city = None
    min_distance = sys.maxsize

    for city in unvisited_cities:
        d = distance(current_city, city)
        if d < min_distance:
            min_distance = d
            nearest_city = city

    return nearest_city, min_distance

# Function to find the shortest TSP tour using Nearest Neighbor Algorithm
def tsp_nearest_neighbor(start_city):
    tour = [start_city]
    unvisited_cities = set(range(1, 5)) - {start_city}

    while unvisited_cities:
        current_city = tour[-1]
        nearest_city, _ = nearest_neighbor(current_city, unvisited_cities)
        tour.append(nearest_city)
        unvisited_cities.remove(nearest_city)

    tour.append(start_city)
    return tour

# Main function
def main():
    start_city = int(input("Enter the starting city (1-4): "))
    if start_city not in range(1, 5):
        print("Invalid input.")
        return

    tour = tsp_nearest_neighbor(start_city)
    print("Shortest TSP Tour using Nearest Neighbor Algorithm:")
    print(" -> ".join(map(str, tour)))
    print("Total Distance:", sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1)))

if __name__ == "__main__":
    main()