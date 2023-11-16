import time
import os


menü = {"çay": 1.5, "tost": 4.0, "limonata": 10.0, "su": 1.0 }

masalar = dict()
smasa = 20    #int(input("kaç masa var : "))	

for a in range(smasa):
	masalar[a] = 0


def ekle():

	print("Number of Table >>> ",smasa-1,"\n")
	
	print("          ","ÜRÜNLER","\n")
	for a in menü.keys():
		print("          ",a)
	print("")
	
	try:
		masaNo = int(input("Masa No. : "))

		if masaNo < smasa and masaNo >= 0 :	
			hesap = float(masalar[masaNo])
			print("Şuanki Hesap >>> ",hesap)
			
			try:
				ürün = input("Ürün Adı : ")
				adet = int(input("Ürün Adeti : "))
				fiyat = menü[ürün]
				ekle = fiyat * adet
					#ekle = input("Eklenecek Tutar : ")
					#ekle = ekle.replace(",",".")
				ghesap = float(ekle) + hesap
				masalar[masaNo] = ghesap
				print("Successfully Added To Bill :D") #, Press Enter For Return")
				#input()
				time.sleep(0.6)

			except KeyError:
					input("Yazdığınız Ürün Menüde Yok ! Tüm Harfleri Küçük Yazmayı Deneyin.")
		
		else:
			input("\nGeçerli Masa Numarası Girin !")
	
	except:
		input("\nGeçerli Masa Numarası Girin !")
		

def çıkar():

	print("Number of Table >>> ",smasa-1,"\n")
	
	print("          ","ÜRÜNLER","\n")
	for a in menü.keys():
		print("          ",a)
	print("")

	try:
		masaNo = int(input("Masa No. : "))
	
		if masaNo < smasa : 
			hesap = float(masalar[masaNo])
			print("Şuanki Hesap >>> ",hesap)
			try:
				ürün = input("Ürün Adı : ")
				adet = float(input("Ürün Adeti : "))
				fiyat = menü[ürün]
				çıkar = adet * fiyat
					#çıkar = input("Çıkarılacak Tutar : ")
					#çıkar = çıkar.replace(",",".")
				ghesap = hesap - float(çıkar)
	
				if ghesap < 0 :
					print("Çıkacak Miktarı Hesaptan Fazla Girdin !")
					input("Ana Menüye Dönmek için Enter'a Bas")
				else:
					masalar[masaNo] = ghesap
					print("Successfully Extracted From Bill :D") #, Press Enter For Return")
				time.sleep(0.6)

			except KeyError:
				input("Ürün Bulunamadı !!")

		else:
			input("\nGeçerli Masa Numarası Girin !")
	
	except ValueError:
		input("Geçerli Masa Numarası Girin !")


def kontrol(dosya_adi):

	try:
		dosya = open(dosya_adi)
		veri = dosya.read()
		veri = veri.split("\n")
		veri.pop()
		dosya.close()
		flag = True
	
	except FileNotFoundError:
		dosya = open(dosya_adi,"w")
		dosya.close()
		print("Program İlk Kez Çalıştı Dosya Oluşturuluyor.")
		time.sleep(2)
		print("Dosya Oluşturuldu.")
		flag = False
	
	if flag:
		for a in enumerate(veri):
			masalar[a[0]] = float(a[1])

	else:
		pass

def yaz():
	dosya = open("Hesaplarr.txt","w")
	for a in range(smasa):
		ücret = masalar[a]
		ücret = str(ücret)
		dosya.write(ücret+"\n")
	dosya.close()

def temizle():
	for a in range(smasa):
		masalar[a] = 0

	time.sleep(1)	
	print("File Is Cleaning")
	time.sleep(1)	
	for i in range(5):
		print(".")
		time.sleep(1)
	time.sleep(1.5)

def ana():

	kontrol("Hesaplarr.txt")
	
	while True:
		os.system("cls")
		yaz()
	
		print("""
	
--------WELCOME TO THE BILLING SYSTEM--------
	
	      1) Masaları Listele
	      2) Hesaba Ekle
	      3) Hesaptan Çıkar
	      4) Listeyi Temizle
	
	      q) Çıkış
	
		""")
	
	
		secim = input("İşlem No. Girin : ")
	
		if secim == "1":

			print("")
			for a in masalar:
				print("masa {} >>>>> {}".format(a,masalar[a]))
			input("\nAna Menüye Dönmek İçin Enter'a Basın")
			
		elif secim == "2":
			ekle()
			
		elif secim == "3":
			çıkar()
			
		elif secim == "4":
			temizle()
			input("File Successfully Cleared, Press Enter For Return")

		elif secim == "q" or secim == "Q":
			os.system("cls")
			quit()

		else:
			input("Please Choose Number In Menu")


ana()