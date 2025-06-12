import numpy as np

def greedy_tsp_np(cities):
    """
    Şehir koordinatlarını içeren 'cities' numpy array'ini kullanarak
    Greedy (açgözlü) TSP algoritmasını uygular.

    Her adımda ziyaret edilmemiş şehirler arasında mesafenin kareleri
    hesaplanarak, en yakın şehir seçilir.

    Args:
        cities (np.ndarray): Şehirlerin (N, 2) boyutunda koordinatları.

    Returns:
        path (list): Başlangıca dönüş dahil oluşturulan TSP turu (şehir indeksleri).
        total_cost (float): Toplam tur mesafesi.
    """
    N = cities.shape[0]
    visited = np.zeros(N, dtype=bool)
    path = [0]           # İlk şehir başlangıç olarak seçiliyor.
    visited[0] = True
    total_cost = 0.0
    current = 0

    for _ in range(N - 1):
        diff = cities - cities[current]
        sq_distances = np.sum(diff**2, axis=1)
        sq_distances[visited] = np.inf  # Ziyaret edilmiş şehirleri dışarıda bırakıyoruz.
        next_city = int(np.argmin(sq_distances))
        dist = np.sqrt(sq_distances[next_city])
        total_cost += dist
        path.append(next_city)
        visited[next_city] = True
        current = next_city

    # Turun kapatılması: Son şehirden başlangıç noktasına dönüş.
    return_dist = np.sqrt(np.sum((cities[current] - cities[path[0]])**2))
    total_cost += return_dist
    path.append(path[0])
    return path, total_cost

def main():
    # Dosya yolunu kendi sisteminize göre ayarlayın.
    file_path = r"C:\Users\selda\OneDrive\Masaüstü\TSP33\TSP_14051_1\tsp_14051_1.text"

    # Dosyayı oku; dosyadaki tüm satırlar şehir koordinatlarını içerir.
    with open(file_path, "r") as f:
        lines = f.readlines()

    cities_list = []
    for line in lines:
        parts = line.split()
        if len(parts) >= 2:
            try:
                x = float(parts[0])
                y = float(parts[1])
                cities_list.append((x, y))
            except:
                continue

    if not cities_list:
        print("Şehir verisi bulunamadı.")
        return

    cities = np.array(cities_list)

    path, cost = greedy_tsp_np(cities)

    # Sadece en iyi yol (şehir indeksleri listesi) ve toplam maliyet ekrana yazdırılır.
    print("En iyi yol:", path)
    print("Toplam maliyet:", cost)

if __name__ == "__main__":
    main()
