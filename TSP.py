import math

def distance(a, b):
    return math.dist(a, b)

def total_distance(tour, cities):
    return sum(distance(cities[tour[i]], cities[tour[i+1]])
               for i in range(len(tour)-1))

def nearest_neighbor(cities):
    n = len(cities)
    visited = [False]*n
    tour = [0]
    visited[0] = True
    
    for _ in range(n-1):
        last = tour[-1]
        next_city = min(
            (i for i in range(n) if not visited[i]),
            key=lambda i: distance(cities[last], cities[i])
        )
        tour.append(next_city)
        visited[next_city] = True
    
    tour.append(tour[0])
    return tour

def two_opt(tour, cities):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour)-2):
            for j in range(i+1, len(tour)-1):
                if j - i == 1:
                    continue
                
                old = (distance(cities[tour[i-1]], cities[tour[i]]) +
                       distance(cities[tour[j]], cities[tour[j+1]]))
                
                new = (distance(cities[tour[i-1]], cities[tour[j]]) +
                       distance(cities[tour[i]], cities[tour[j+1]]))
                
                if new < old:
                    tour[i:j+1] = reversed(tour[i:j+1])
                    improved = True
    return tour

# ---- User Input Section ----
n = int(input("Enter number of cities: "))
cities = []

print("Enter coordinates (x y) for each city:")
for i in range(n):
    x, y = map(float, input(f"City {i}: ").split())
    cities.append((x, y))

# Run nearest neighbor + 2-opt
tour = nearest_neighbor(cities)
tour = two_opt(tour, cities)

print("\nOptimized Tour:", tour)
print("Total Distance:", total_distance(tour, cities))
