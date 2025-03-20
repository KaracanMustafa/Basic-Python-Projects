def cevirici(sayi):
    sayi2=0
    while sayi>0:
        sayi2=int(sayi%10)
        sayi=int(sayi/10)
        print(sayi2,end='')

cevirici(123456789)