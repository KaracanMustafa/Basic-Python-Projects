import random

def sayi_tahmin_oyunu():
    rastgele_sayi=random.randint(1,100)
    tahmin=None
    print("====1 ile 100 arasında sayıyı tahmin et====")

    while tahmin!=rastgele_sayi:
        tahmin=int(input("Tahmininizi girin: "))
        if tahmin>rastgele_sayi:
            print("Daha küçük!")
        if tahmin<rastgele_sayi:
            print("Daha büyük!")

    if tahmin == rastgele_sayi:
        print("Tebrikler Doğru Bildiniz !!!")

sayi_tahmin_oyunu()