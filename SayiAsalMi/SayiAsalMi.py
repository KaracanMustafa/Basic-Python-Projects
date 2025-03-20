def sayi_asal_mi(sayi):
    sayac=0
    i=1
    while i<=sayi:
        if sayi%i==0:
            sayac=sayac+1
        i=i+1
    if sayac==2:
        print(str(sayi)+" sayısı asaldır")
    else:
        print(str(sayi)+" sayısı asal değildir.")

sayi_asal_mi(997)