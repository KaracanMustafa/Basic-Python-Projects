import string
import random

def sifre_olusturucu(uzunluk):
    sifre=''.join(random.choice(string.ascii_letters + string.digits) for _ in range(uzunluk))
    print(sifre)

sifre_olusturucu(8)