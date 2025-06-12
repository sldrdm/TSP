import math
import random
import time

# Koordinatlar (51 şehir)
coordinates = [
    (27, 68), (30, 48), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (46, 10), (61, 33), (62, 63),
    (63, 69), (32, 22), (45, 35), (59, 15), (5, 6), (10, 17), (21, 10), (5, 64), (30, 15), (39, 10),
    (32, 39), (25, 32), (25, 55), (48, 28), (56, 37), (30, 40), (37, 52), (49, 49), (52, 64), (20, 26),
    (40, 30), (21, 47), (17, 63), (31, 62), (52, 33), (51, 21), (42, 41), (31, 32), (5, 25), (12, 42),
    (36, 16), (52, 41), (27, 23), (17, 33), (13, 13), (57, 58), (62, 42), (42, 57), (16, 57), (8, 52), (7, 38)
]

# Mesafe hesabı
def distance(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def total_distance(path):
    dist = 0
    for i in range(len(path)):
        dist += distance(coordinates[path[i]], coordinates[path[(i+1)%len(path)]])
    return dist

# 2-opt iyileştirme
def two_opt(route):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(route) - 2):
            for j in range(i + 1, len(route)):
                if j - i == 1:
                    continue
                new_route = route[:]
                new_route[i:j] = reversed(route[i:j])
                if total_distance(new_route) < total_distance(route):
                    route = new_route
                    improved = True
    return route

# Kaotik lojistik harita
def chaotic_map(size):
    x = random.random()
    seq = []
    for _ in range(size):
        x = 4 * x * (1 - x)  # Logistic map
        seq.append(x)
    return seq

# Başlangıç popülasyonu üret
def create_population(n_individuals, n_cities):
    pop = []
    for _ in range(n_individuals):
        route = list(range(n_cities))
        random.shuffle(route)
        pop.append(route)
    return pop

# Ana CSSA fonksiyonu
def cssa_tsp(pop_size=100, iterations=300):
    num_cities = len(coordinates)
    population = create_population(pop_size, num_cities)
    best_solution = min(population, key=total_distance)
    best_cost = total_distance(best_solution)

    for t in range(iterations):
        chaotic_seq = chaotic_map(pop_size)
        sorted_indices = sorted(range(pop_size), key=lambda i: chaotic_seq[i])
        discoverers = sorted_indices[:int(0.2 * pop_size)]
        joiners = sorted_indices[int(0.2 * pop_size):]

        for i in discoverers:
            if random.random() < 0.9:
                new_solution = population[i][:]
                i1, i2 = sorted(random.sample(range(num_cities), 2))
                new_solution[i1:i2] = reversed(new_solution[i1:i2])
                if total_distance(new_solution) < total_distance(population[i]):
                    population[i] = new_solution

        for i in joiners:
            peer = random.choice(discoverers)
            new_solution = population[i][:]
            for swap in range(1, num_cities - 1):
                if random.random() < 0.3:
                    city = population[peer][swap]
                    idx = new_solution.index(city)
                    new_solution[swap], new_solution[idx] = new_solution[idx], new_solution[swap]
            if total_distance(new_solution) < total_distance(population[i]):
                population[i] = new_solution

        current_best = min(population, key=total_distance)
        current_cost = total_distance(current_best)
        if current_cost < best_cost:
            best_solution = current_best
            best_cost = current_cost

    # Final iyileştirme
    best_solution = two_opt(best_solution)
    best_cost = total_distance(best_solution)
    return best_solution, best_cost

# Ana çalıştırma
if __name__ == "__main__":
    start = time.time()
    path, cost = cssa_tsp()
    duration = time.time() - start

    path_str = " -> ".join(str(city) for city in path + [path[0]])
    print(f"\nEn iyi yol: {path_str}")
    print(f"Toplam mesafe: {cost:.2f}")
    print(f"Hesaplama süresi: {duration:.2f} saniye")


