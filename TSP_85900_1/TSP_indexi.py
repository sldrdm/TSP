import numpy as np
from scipy.spatial import cKDTree
import math

def read_points_from_file(file_path):
    """
    Dosyayı okuyup, içerisindeki nokta koordinatlarını NumPy dizisi olarak döndürür.
    Eğer dosyanın ilk satırında tek sayı varsa (örneğin nokta sayısı), buna göre satırlar ayrılır.
    """
    with open(file_path, 'r') as f:
        lines = f.readlines()

    # İlk satır tek sayı içeriyorsa (örneğin: "85900") ve kalan satır sayısı bu sayıya eşitse
    first_line = lines[0].strip().split()
    if len(first_line) == 1:
        try:
            num_points = int(first_line[0])
            if len(lines[1:]) == num_points:
                data = np.loadtxt(lines[1:])
            else:
                data = np.loadtxt(lines)
        except ValueError:
            data = np.loadtxt(lines)
    else:
        data = np.loadtxt(lines)

    return np.array(data, dtype=float)

def greedy_tsp_kdtree(points):
    """
    cKDTree kullanılarak greedy algoritması ile TSP çözümü.
    - Başlangıç olarak 0. indeksli nokta seçilir.
    - Her iterasyonda, cKDTree üzerinden yakın komşular sorgulanır ve henüz ziyaret edilmemiş olan
      adaylar arasından en yakını seçilir.
    - Son olarak başlangıç noktasına dönüş eklenir.

    Returns:
        tour (list): Ziyaret sırasındaki nokta indeksleri (başlangıç tekrarı ile).
        total_cost (float): Oluşan turun toplam mesafesi (maliyet).
    """
    n = points.shape[0]
    visited = np.zeros(n, dtype=bool)
    tour = []
    current_index = 0
    tour.append(current_index)
    visited[current_index] = True
    total_cost = 0.0

    # Tüm noktaları içeren KD-Tree'yi oluştur
    kd_tree = cKDTree(points)

    for i in range(n - 1):
        k = 2  # İlk sorguda 2 komşu sorguluyoruz (ilk komşu kendimiz olur)
        found = False
        while not found:
            distances, indices = kd_tree.query(points[current_index], k=k)
            # Eğer k==1 ise, array tipini standartlaştırıyoruz
            distances = np.atleast_1d(distances)
            indices = np.atleast_1d(indices)
            for d, j in zip(distances, indices):
                if j == current_index:
                    continue  # Kendi noktamız atlanır
                if not visited[j]:
                    next_index = j
                    next_distance = d
                    found = True
                    break
            if not found:
                # Eğer aday bulunamadıysa, komşu sayısını artırıyoruz
                k = min(k * 2, n)
                if k == n:
                    # Tüm noktalar sorgulandığında bile hiçbir aday bulunamazsa (teoride olmaz)
                    unvisited = np.where(~visited)[0]
                    distances_full = np.linalg.norm(points[unvisited] - points[current_index], axis=1)
                    min_idx = np.argmin(distances_full)
                    next_index = unvisited[min_idx]
                    next_distance = distances_full[min_idx]
                    found = True
        total_cost += next_distance
        tour.append(next_index)
        visited[next_index] = True
        current_index = next_index

    # Turun sonunda başlangıç noktasına dönüş ekleniyor
    return_distance = np.linalg.norm(points[current_index] - points[tour[0]])
    total_cost += return_distance
    tour.append(tour[0])

    return tour, total_cost

if __name__ == "__main__":
    # Verisetinizin dosya yolu (direkt sayılarla path çıktısı verilecek)
    file_path = r"C:\Users\selda\OneDrive\Masaüstü\TSP33\TSP_85900_1\tsp_85900_1.text"
    points = read_points_from_file(file_path)

    if points.size == 0 or points.ndim != 2 or points.shape[1] != 2:
        print("Veri kümesinde geçerli nokta koordinatları bulunamadı.")
    else:
        tour, cost = greedy_tsp_kdtree(points)
        # Tur çıktısını doğrudan sayılar şeklinde, boşlukla ayrılmış olarak yazdırıyoruz
        print("Greedy algoritmasıyla oluşturulan rota (nokta indeksleri):")
        print(" ".join(map(str, tour)))
        print("\nToplam maliyet (tur uzunluğu): {:.2f}".format(cost))
