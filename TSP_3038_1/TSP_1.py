
"""
NumPy kütüphanesini içe aktarır, bilimsel hesaplamalar ve dizi işlemleri için gerekli olan temel matematiksel işlevleri sağlar.

NumPy, Python'da yüksek performanslı sayısal hesaplamalar için kullanılan bir kütüphanedir. Bu içe aktarma işlemi, matris operasyonları, matematiksel fonksiyonlar ve verimli dizi işlemleri için gereklidir.

Özellikler:
- Çok boyutlu dizi desteği
- Matematiksel ve istatistiksel fonksiyonlar
- Lineer cebir işlemleri
- Hızlı ve verimli hesaplama yetenekleri

Bu modülde, TSP (Gezgin Satıcı Problemi) çözümünde koordinat hesaplamaları ve mesafe matris işlemleri için kullanılacaktır.
"""


import numpy as np

def read_coordinates(filename):
    # Dosyayı açar, satırları okur ve her satırdaki ilk iki sayıyı (x, y) almak üzere işler.
    coords = []
    with open(filename, "r") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) >= 2:
                try:
                    x = float(parts[0])
                    y = float(parts[1])
                    coords.append([x, y])
                except:
                    continue
    return np.array(coords)

def calc_distance_matrix(coords):
    # İki şehir arasındaki Öklid mesafelerini hesaplayarak n x n boyutlu mesafe matrisi oluşturur.
    diff = coords[:, None, :] - coords[None, :, :]
    return np.sqrt(np.sum(diff**2, axis=2))

def total_cost(tour, dist):
    # Vektörleştirilmiş şekilde, turun toplam maliyetini hesaplar.
    tour = np.array(tour)
    return np.sum(dist[tour[:-1], tour[1:]])

def two_opt(tour, dist):
    # Temel 2-opt algoritmasıyla turu iyileştirir.
    improved = True
    n = len(tour) - 1  # sondaki tekrarı hariç tutar
    while improved:
        improved = False
        for i in range(1, n - 1):
            for j in range(i + 1, n):
                a, b = tour[i - 1], tour[i]
                c, d = tour[j], tour[(j + 1) % len(tour)]
                if dist[a, c] + dist[b, d] < dist[a, b] + dist[c, d]:
                    tour[i:j+1] = tour[i:j+1][::-1]
                    improved = True
        # İyileştirme olmazsa döngü sonlanır.
    return tour

def main():
    # Dosya yolunu kendi ortamınıza göre düzenleyin:
    filename = r"C:\Users\selda\OneDrive\Masaüstü\TSP33\TSP_3038_1\tsp_3038_1.text"
    coords = read_coordinates(filename)
    dist = calc_distance_matrix(coords)
    n = coords.shape[0]

    # İlk tur: 0, 1, 2, ..., n-1 ve ardından başlangıca dönüş
    tour = list(range(n))
    tour.append(tour[0])

    optimized_tour = two_opt(tour, dist)
    cost = total_cost(optimized_tour, dist)

    # Sadece optimal maliyeti ve optimal tur path'ini ekrana yazdırır.
    print("Optimal maliyet:", cost)
    print("Optimal tur yolu (şehir endeksleri):", optimized_tour)

if __name__ == "__main__":
    main()

