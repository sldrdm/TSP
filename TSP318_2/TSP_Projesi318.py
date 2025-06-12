import numpy as np

def read_points_from_file(file_path):
    """
    Dosyayı okuyup içerisindeki nokta koordinatlarını NumPy dizisine çevirir.
    Eğer dosyanın ilk satırında tek sayı (örn. nokta sayısı) varsa ve kalan satır sayısı buna uyuyorsa,
    bu durumda ilk satır atlanır.
    """
    with open(file_path, "r") as f:
        lines = f.readlines()
    first_line = lines[0].strip().split()
    if len(first_line) == 1:
        try:
            num_points = int(first_line[0])
            # Dosyadaki satır sayısı, ilk satır (n) + koordinat satırları (num_points) şeklinde ise
            if len(lines[1:]) == num_points:
                data = np.loadtxt(lines[1:])
            else:
                data = np.loadtxt(lines)
        except:
            data = np.loadtxt(lines)
    else:
        data = np.loadtxt(lines)
    return np.array(data, dtype=float)

def compute_distance_matrix(points):
    """
    Tüm şehirler arasındaki Öklidyen mesafeyi hesaplayıp bir distance matrix oluşturur.
    Her (i, j) elemanı, points[i] ile points[j] arasındaki mesafeyi içerir.
    """
    diff = points[:, np.newaxis, :] - points[np.newaxis, :, :]
    return np.sqrt(np.sum(diff**2, axis=2))

def total_distance(route, distance_matrix):
    """
    Verilen rota (şehir indeksleri listesi) için, distance matrix kullanarak
    kapalı turun (başlangıçtan başlayıp yine başlangıca dönen) toplam mesafesini hesaplar.
    """
    n = len(route)
    total = 0.0
    for i in range(n - 1):
        total += distance_matrix[route[i], route[i+1]]
    # Son şehirden ilk şehre dönüş mesafesi eklenir
    total += distance_matrix[route[-1], route[0]]
    return total

def two_opt_vectorized(route, distance_matrix, tol=1e-9):
    """
    Vektörleştirilmiş iç döngü kullanarak 2‑opt algoritması ile rotayı optimize eder.

    Başlangıçta sıralı olarak verilen rotada (0, 1, 2, …) yerel delta farklarına bakılarak,
    iki kenarın ters çevrilmesi sonucu elde edilecek mesafe farkı (delta) hızlıca hesaplanır.
    Eğer herhangi bir ters çevirme, toplam mesafeyi azaltıyorsa, swap uygulanır.
    İyileştirme sağlanmayıncaya kadar döngü devam eder.
    """
    n = len(route)
    best_route = route.copy()
    best_cost = total_distance(best_route, distance_matrix)
    improved = True
    best_route_arr = np.array(best_route)

    while improved:
        improved = False
        # İlk şehir sabit kalacağından i = 1'den başlıyoruz
        for i in range(1, n - 1):
            # j adayları: i+1 ... n-1
            j_candidates = np.arange(i + 1, n)
            a = best_route[i - 1]                    # Sabit
            b = best_route[i]                        # Sabit
            c = best_route_arr[j_candidates]         # Vektörel candidate c değerleri
            d = best_route_arr[(j_candidates + 1) % n]  # d değerleri; j+1 için mod n
            # Hesaplanan delta: d(a, c) + d(b, d) - d(a, b) - d(c, d)
            delta = distance_matrix[a, c] + distance_matrix[b, d] \
                    - distance_matrix[a, b] - distance_matrix[c, d]

            # Min delta, eğer negatif ise iyileştirme potansiyeli var
            min_delta = np.min(delta)
            if min_delta < -tol:
                # İyileştirme var; en iyi j adayı bulunur
                best_j = j_candidates[np.argmin(delta)]
                # Ters çevirme (reverse) işlemi
                best_route[i:best_j + 1] = best_route[i:best_j + 1][::-1]
                best_cost += min_delta
                improved = True
                best_route_arr = np.array(best_route)  # Güncellenmiş rotayı diziye aktar
                break  # Dış döngüye geri dönerek i'yi güncelle

    return best_route, best_cost

if __name__ == '__main__':
    # Dosya yolunu kendi sisteminize göre değiştirin.
    file_path = r"C:\Users\selda\OneDrive\Masaüstü\TSP33\TSP318_2\tsp_318_2.text"
    points = read_points_from_file(file_path)

    if points.size == 0 or points.ndim != 2 or points.shape[1] != 2:
        print("Veri kümesinde geçerli nokta koordinatları bulunamadı.")
    else:
        n = len(points)
        # Başlangıç rotasını, şehirleri sıralı olarak (0, 1, 2, …) kabul ediyoruz.
        initial_route = list(range(n))
        # Şehirler arası mesafe matrisini hesapla.
        distance_matrix = compute_distance_matrix(points)

        # 2‑opt algoritmasıyla (ve vektörleştirilmiş iç döngüyle) rota optimizasyonu.
        best_route, best_cost = two_opt_vectorized(initial_route, distance_matrix)

        # Ekranda da “ilk şehre dönüşü” açıkça görmek için rotanın sonuna tekrar ilk şehri ekleyelim.
        final_route = best_route.copy()
        final_route.append(final_route[0])

        print("Optimal tur (nokta indeksleri) (başlangıç şehrine geri dönüş dahil):")
        print(" -> ".join(map(str, final_route)))
        print(f"Optimal toplam maliyet (tur uzunluğu): {best_cost:.2f}")
