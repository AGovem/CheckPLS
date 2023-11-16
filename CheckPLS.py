import time

reset = '\33[m'
kırmızı = '\33[31m'
yeşil = '\33[32m'
sarı = '\33[33m'
mavi = '\33[34m'
mor = '\33[35m'
beyaz = '\33[37m'

masalar = dict()
masasayi = 20

for i in range(masasayi):
    masalar[i+1] = 0
#print(masalar)
def ana():
    print("""
            -----------ANA MENÜ----------- 
                1) Ücret Ekle
                2) Ücret Çıkar
                3) Hesapları Göster
                4) Hesabı İstenen Masa

                q) Çıkış
            """)


def ekle():
    try:
        masano = input("Masa Numarası (Menüye Dönmek İçin 'b') : ")

        if masano == "b" or masano == "B":
            return ana()
        if int(masano) <= masasayi:
            masano = int(masano)
            hesap = masalar[masano]
            try:
                eklenecek = input("eklenecek tutar : ")
                eklenecek = eklenecek.replace(",",".")
                yhesap = hesap + float(eklenecek)
                masalar[masano] = yhesap
                print("\33[34m", "Güncel Hesap : ", '\33[m', "{}".format(yhesap))
                time.sleep(1.5)
            except:
                print("\33[31m",'\33[1m',"Girdiğiniz Tutar Sayı Olmalı","\33[m")                              #       UYARI
                time.sleep(1.5)
    except:
        print("\n",'\033[31m','\33[1m',"Masa Numarası Tam Sayı Olmalı!",'\33[m')                              #       UYARI
        time.sleep(3)

def cikar():
    try:
        masano = input("Masa Numarası (Menüye Dönmek İçin 'b') : ")
        if masano == "b" or masano == "B":
            return ana()
        if int(masano) <= masasayi:
            masano = int(masano)
            hesap = masalar[masano]
            try:
                cikarilacak = input("çıkarılacak miktar : ")
                cikarilacak = cikarilacak.replace(",",".")
                yhesap = hesap - float(cikarilacak)
                if yhesap < 0:
                    print('\33[31m' ,'\33[1m',"hesap sıfırdan küçük olamaz !", '\33[m')                              #       UYARI
                    return cikar()
                masalar[masano] = yhesap
                print("\33[34m", "Güncel Hesap : ", '\33[1m', "{}".format(yhesap),'\33[m')
                time.sleep(1.5)
            except:
                print("\33[31m",'\33[1m',"Girdiğiniz Tutar Sayı Olmalı","\33[m")                             #       UYARI
                time.sleep(1.5)
    except:
        print("\n", '\033[31m','\33[1m', "Masa Numarası Tam Sayı Olmalı!", '\33[m')                          #       UYARI
        time.sleep(3)

def goster():
    try:
        masano = int(input("masa numarası : "))
        if masano <= masasayi:
            print(masalar[masano])
        else:
            input("Yanlış Giriş Yaptınız!! Menüye Dönüş İçin Enter'a Basınız. ")
        input()
    except:
        print("\n", '\033[31m','\33[1m', "Masa Numarası Tam Sayı Olmalı!", '\33[m')                  #     UYARI
        time.sleep(3)

def tumgoster():
    for s in masalar:
        print("Masa {} >>>>>>>>>>> {} TL".format(s,masalar[s]))
    input()

while True:
    ana()
    try:
        a = input("işlemi seç : ")

        if a == "q":
            a = str(a)
        else:
            a = int(a)

        if a == 1:
            ekle()

        elif a == 2:
            cikar()

        elif a == 3:
            tumgoster()

        elif a == 4:
            goster()

        elif a == "q" or "Q":
            break
    except:
        print("\33[31m",'\33[1m',"Lütfen Menüdeki Değerlerden Birini Girin!!","\33[m")
        time.sleep(2)