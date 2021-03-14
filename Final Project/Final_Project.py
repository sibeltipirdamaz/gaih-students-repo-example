puan=0

bir = input("Türkiye'nin başkenti nedir? ")
if bir == "Ankara":
  puan+=10
  print("Doğru cevap!")
else:
  print("Yanlış cevap!")

iki = input("En büyük uydusu olan gezegen nedir? ")
if iki == "Jüpiter":
  puan+=10
  print("Doğru cevap!")
else:
  print("Yanlış cevap!")

üç = input("Hava sıcaklığını ölçen cihaz nedir? ")
if üç == "Termometre":
  puan+=10
  print("Doğru cevap!")
else:
  print("Yanlış cevap!")

dört = input("1'in türevi kaçtır? ")
if dört == "0":
  puan+=10
  print("Doğru cevap!")
else:
  print("Yanlış cevap!")

beş = input("Dünyadaki en büyük kıta hangisidir? ")
if beş == "Asya":
  puan+=10
  print("Doğru cevap!")
else:
  print("Yanlış cevap!")

altı = input("Yaşayan en büyük hayvan nedir? ")
if altı == "Mavi balina":
  puan+=10
  print("Doğru cevap!")
else:
  print("Yanlış cevap!")

yedi = input("Örümceklerin kaç bacağı vardır? ")
if yedi == "Sekiz":
  puan+=10
  print("Doğru cevap!")
else:
  print("Yanlış cevap!")

sekiz = input("Türkiye'nin kaç komşu ülkesi vardır? ")
if sekiz == "Sekiz":
  puan+=10
  print("Doğru cevap!")
else:
  print("Yanlış cevap!")

dokuz = input("En kalabalık ülke hangisidir? ")
if dokuz == "Çin":
  puan+=10
  print("Doğru cevap!")
else:
  print("Yanlış cevap!")

on = input("Yüzölçümü en küçük ülke hangisidir? ")
if on == "Vatikan":
  puan+=10
  print("Doğru cevap!")
else:
  print("Yanlış cevap!")

if puan>50:
  print("Başarılı")
else:
  print("Başarısız")
