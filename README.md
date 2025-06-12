  TSP Probleminin Tanımı
 Gezgin Satıcı Problemi (TSP), bir satıcının belirli bir şehirden başlayarak her bir şehri
 yalnızca bir kez ziyaret ettikten sonra tekrar başlangıç noktasına döndüğü en kısa
 rotayı bulma problemidir. Başka bir deyişle, TSP, verilen n adet şehir (düğüm) ve bu şehirler
 arasındaki mesafeler veya maliyetlerle tanımlanan bir ağ içerisinde, toplam yol uzunluğunu
 (veya maliyeti) minimize eden kapalı bir tur (rota) arayışıdır.
 Matematiksel bakımdan, TSP şehirlerin düğümler; şehirlerarası yolların kenarlar olarak
 temsil edildiği bir çizge üzerinde en kısa Hamilton döngüsünü (her düğümü tam bir
 kez ziyaret edip başlangıç noktasına dönen yol) bulmayı hedefler. TSP farklı biçimlerde
 matematiksel olarak modellenebilir. Örneğin bir tamsayılı doğrusal programlama (integer
 linear programming) problemi şeklinde ifade edilmesi yaygındır ve bu kapsamda Miller–
 Tucker–Zemlin (MTZ) ile Dantzig–Fulkerson–Johnson (DFJ) gibi formülasyonlar öne
 çıkar.
 Bu modellerde, her şehrin sadece bir defa ziyaret edilmesi ve başlangıç noktasına geri
 dönülmesi, karar değişkenleri ve kısıtlar yardımıyla sağlanır. MTZ ve DFJ formülasyonları,
 özellikle alt turları engelleyen kısıtlar sayesinde tek bir Hamilton turu elde edilmesini garanti
 eder. Dolayısıyla TSP, hem sezgisel bir rota optimizasyonu yaklaşımıyla anlaşılabilir hem de
 katı matematiksel kısıtlarla modellenebilen bir problemdir.
 
  TSP’nin Önemi
 TSP, hesaplama kuramında ve optimizasyon alanında önemli bir yere sahip olup, NPzor (NP-hard) problemler sınıfında bulunur. Dolayısıyla şehir sayısı arttıkça (özellikle
 büyük n değerlerinde) tam çözüm bulmak üstel (exponential) karmaşıklığa yol açtığından
 pratik olarak imkânsız hale gelebilir. Bunun yanı sıra TSP, P = NP? gibi büyük tartışmaların odak noktalarından biri olarak teorik bilgisayar bilimi açısından da merkezi bir
 konumdadır.
 TSP’nin bir diğer önemli noktası, araştırma ve karşılaştırma çalışmalarında bir mihenk
 taşı (benchmark) görevi görmesidir. Özellikle yöneylem araştırması ve meta-sezgisel
 (metaheuristic) algoritmalar alanında, yeni geliştirilen yöntemlerin test edilmesi için ilk
 başvurulan klasik problemlerdendir. TSP ayrıca, kombinatoryal optimizasyon ve graf
 teorisi konularında önemli bir referans noktasıdır.
 
 TSP Problemi İçin Yeni Bir Kaos Serçesi Arama Algoritması
 (A Novel Chaos Sparrow Search Algorithm for TSP Problem)
 Bu çalışmada, Gezgin Satıcı Problemi için geliştirilen Yeni Kaos Serçesi Arama Algoritması (NCSSA) tanıtılmıştır. NCSSA, kaotik başlangıç, gelişmiş konum güncelleme ve çeşitli
 mutasyon stratejileri ile yerel optimumlardan kaçınmayı hedeflemektedir. TSPLIB verileriyle
 yapılan karşılaştırmalarda, NCSSA hem çözüm doğruluğu hem de hız açısından ACO ve
 DBA algoritmalarına üstünlük sağlamıştır. Yöntem, gerçek dünya uygulamaları için etkili
 bir optimizasyon aracı olarak öne çıkmaktadır.
 
 51 Şehir Travel Salesman Problem Sonuç Çıktısı
 • Kullanılan Yöntem: A Novel Chaos Sparrow Search Algorithm
 • Optimal Maliyet: 474.42
 • En İyi Çözüm Rotası (ilk birkaç şehir):
 41 -> 34 -> 23 -> 30 -> 12 -> 36 -> 6 -> 1 -> 25 -> 20 -> ...
