def kelime_ayirici(cumle):
    kelimeler=cumle.split()
    kelime_sayisi=len(kelimeler)
    print("Toplam kelime sayısı: ",kelime_sayisi)

cumle=input("Bir cümle giriniz: ")
kelime_ayirici(cumle)