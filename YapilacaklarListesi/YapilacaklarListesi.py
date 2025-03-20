import json

# Görevleri saklamak için bir liste
gorevler = []

# Dosyadan görevleri yükleyen fonksiyon
def gorevleri_yukle():
    try:
        with open("gorevler.json", "r") as dosya:
            global gorevler
            gorevler = json.load(dosya)
    except FileNotFoundError:
        gorevler = []

# Görevleri dosyaya kaydeden fonksiyon
def gorevleri_kaydet():
    with open("gorevler.json", "w") as dosya:
        json.dump(gorevler, dosya)

# Görev ekleyen fonksiyon
def gorev_ekle():
    baslik = input("Görev başlığı: ")
    aciklama = input("Görev açıklaması (isteğe bağlı): ")
    gorevler.append({"baslik": baslik, "aciklama": aciklama, "tamamlandi": False})
    print("Görev eklendi.")

# Görevleri listeleyen fonksiyon
def gorevleri_listele():
    if not gorevler:
        print("Hiçbir görev yok.")
    else:
        for i, gorev in enumerate(gorevler, 1):
            durum = "[X]" if gorev["tamamlandi"] else "[ ]"
            print(f"{i}. {durum} {gorev['baslik']} - {gorev['aciklama']}")

# Görevi tamamlandı olarak işaretleyen fonksiyon
def gorev_tamamla():
    gorev_numarasi = int(input("Tamamlanan görevin numarasını girin: "))
    if 1 <= gorev_numarasi <= len(gorevler):
        gorevler[gorev_numarasi - 1]["tamamlandi"] = True
        print("Görev tamamlandı olarak işaretlendi.")
    else:
        print("Geçersiz görev numarası.")

# Görev silen fonksiyon
def gorev_sil():
    gorev_numarasi = int(input("Silinecek görevin numarasını girin: "))
    if 1 <= gorev_numarasi <= len(gorevler):
        gorevler.pop(gorev_numarasi - 1)
        print("Görev silindi.")
    else:
        print("Geçersiz görev numarası.")

# Ana program
gorevleri_yukle()
while True:
    print("\nYapılacaklar Listesi:")
    print("1. Görevleri listele")
    print("2. Görev ekle")
    print("3. Görevi tamamla")
    print("4. Görev sil")
    print("5. Çıkış")
    secim = input("Seçiminizi yapın: ")

    if secim == "1":
        gorevleri_listele()
    elif secim == "2":
        gorev_ekle()
    elif secim == "3":
        gorev_tamamla()
    elif secim == "4":
        gorev_sil()
    elif secim == "5":
        gorevleri_kaydet()
        print("Görevler kaydedildi. Çıkılıyor...")
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
