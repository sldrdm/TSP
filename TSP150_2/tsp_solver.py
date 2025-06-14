import math
import matplotlib.pyplot as plt

# Şehir koordinatları (x, y)
cities = [
    (3099, 173), (2178, 978), (138, 1610), (2082, 1753), (2302, 1127), (805, 272),
    (22, 1617), (3213, 1085), (99, 536), (1533, 1780), (3564, 676), (29, 6),
    (3808, 1375), (2221, 291), (3499, 1885), (3124, 408), (781, 671), (1027, 1041),
    (3249, 378), (3297, 491), (213, 220), (721, 186), (3736, 1542), (868, 731),
    (960, 303), (3825, 1101), (2779, 435), (201, 693), (2502, 1274), (765, 833),
    (3105, 1823), (1937, 1400), (3364, 1498), (3702, 1624), (2164, 1874),
    (3019, 189), (3098, 1594), (3239, 1376), (3359, 1693), (2081, 1011),
    (1398, 1100), (618, 1953), (1878, 59), (3803, 886), (397, 1217), (3035, 152),
    (2502, 146), (3230, 380), (3479, 1023), (958, 1670), (3423, 1241), (78, 1066),
    (96, 691), (3431, 78), (2053, 1461), (3048, 1), (571, 1711), (3393, 782),
    (2835, 1472), (144, 1185), (923, 108), (989, 1997), (3061, 1211), (2977, 39),
    (1668, 658), (878, 715), (678, 1599), (1086, 868), (640, 110), (3551, 1673),
    (106, 1267), (2243, 1332), (3796, 1401), (2643, 1320), (48, 267), (1357, 1905),
    (2650, 802), (1774, 107), (1307, 964), (3806, 746), (2687, 1353), (43, 1957),
    (3092, 1668), (185, 1542), (834, 629), (40, 462), (1183, 1391), (2048, 1628),
    (1097, 643), (1838, 1732), (234, 1118), (3314, 1881), (737, 1285), (779, 777),
    (2312, 1949), (2576, 189), (3078, 1541), (2781, 478), (705, 1812), (3409, 1917),
    (323, 1714), (1660, 1556), (3729, 1188), (693, 1383), (2361, 640), (2433, 1538),
    (554, 1825), (913, 317), (3586, 1909), (2636, 727), (1000, 457), (482, 1337),
    (3704, 1082), (3635, 1174), (1362, 1526), (2049, 417), (2552, 1909),
    (3939, 640), (219, 898), (812, 351), (901, 1552), (2513, 1572), (242, 584),
    (826, 1226), (3278, 799), (86, 1065), (14, 454), (1327, 1893), (2773, 1286),
    (2469, 1838), (3835, 963), (1031, 428), (3853, 1712), (1868, 197),
    (1544, 863), (457, 1607), (3174, 1064), (192, 1004), (2318, 1925),
    (2232, 1374), (396, 828), (2365, 1649), (2499, 658), (1410, 307), (2990, 214),
    (3646, 1018), (3394, 1028), (1779, 90), (1058, 372), (2933, 1459)
]

def distance(a, b):
    return math.dist(cities[a], cities[b])

def total_path_cost(path):
    return sum(distance(path[i], path[i+1]) for i in range(len(path)-1)) + distance(path[-1], path[0])

def nearest_neighbor_path():
    unvisited = set(range(1, len(cities)))
    path = [0]
    current = 0
    while unvisited:
        next_city = min(unvisited, key=lambda x: distance(current, x))
        path.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    return path

def two_opt(path):
    best = path
    improved = True
    while improved:
        improved = False
        for i in range(1, len(path) - 2):
            for j in range(i + 1, len(path)):
                if j - i == 1:
                    continue
                new_path = best[:i] + best[i:j][::-1] + best[j:]
                if total_path_cost(new_path) < total_path_cost(best):
                    best = new_path
                    improved = True
        path = best
    return best

# Çözüm üretimi
initial_path = nearest_neighbor_path()
optimized_path = two_opt(initial_path)
optimized_cost = total_path_cost(optimized_path)

# Sonuç
print("Optimal Path:", optimized_path + [optimized_path[0]])  # Dönüş eklendi
print("Total Cost:", round(optimized_cost, 2))

# Görselleştir
x = [cities[i][0] for i in optimized_path + [optimized_path[0]]]
y = [cities[i][1] for i in optimized_path + [optimized_path[0]]]

plt.figure(figsize=(12, 8))
plt.plot(x, y, marker='o')
plt.title('Optimized TSP Path (KNN + 2-opt)')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.grid(True)
plt.show()
