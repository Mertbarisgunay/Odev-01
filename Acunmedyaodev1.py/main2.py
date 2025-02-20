#video2

faiz = 1.59 
vade = "35"
krediAdi = "İhtiyaç Kredisi"

print(type(faiz))
print(type(vade))
print(type(krediAdi))

print(int(vade) + 12)
faiz=str(faiz)
print(type(faiz))

# vade = int(input("Lütfen İstediğiniz Vade Sayısını Giriniz"))
print(type(vade))
print(int(vade) + 12)

# string interpolation
# Seçtiğiniz vade sonucu ortaya çıkan vade:

print("seçtiğiniz vade sonucu ortaya çıkan vade: " + str(vade))
print("seçtiğiniz vade sonucu ortaya çıkan vade:  {vadeSayisi}" . format (vadeSayisi=vade))


isim = "mert"
metin = "merhaba {name}".format(name=isim)
print(metin)

#f-string

metin = f"hoşgeldiniz {1+1}"
print(metin)


# listeler
# döngüler
# fonksiyonlar

krediler = ["ihtiyaç kredisi", "taşıt kredisi", "konut kredisi"]
print(type(krediler))

print(krediler[0])
print(krediler[2])

print(len(krediler)) #length, uzunluk

dizi = ["İhtiyaç Kredisi", 10, 5.2, True]
print(dizi)


krediler.pop(0)
print(krediler)

krediler.append("taşıt kredisi")
print(krediler)

krediler.remove("taşıt kredisi")
print(krediler)

krediler.extend(["y kredisi", "x kredisi"])
print(krediler)


# for
# i=0 i<10

for i in range(10):
    print("xx")
    print(i)
print("---------------------------")
for i in range(0,51,10):
    print(i)
print("---------------------------")

krediler = ["ihtiyaç kredisi", "taşıt kredisi", "konut kredisi"]

for kredi in krediler:
    print(kredi)
print("---------------------------")

for i in range(len(krediler)):
    print(krediler[i])
print("---------------------------")

i=0
while i<10:
    print("x")
    i = i + 1
print("y")

while True:
    print("x")
    break

print("---------------------------")

i = 0
while i < len(krediler):
    i = i + 1
    print(i)
    print(krediler[i])
    if krediler[i] == "konut kredisi":
      break


#fonksiyonlar

fiyat = 100
indirim = 20

#definition define

def calculate():
    print(100-20)

def calculateWithParams(fiyat, indirim):
    print(fiyat-indirim)    

def sayHello(name):
    print(f"merhaba{name}")

calculate()
calculateWithParams(50,10)
calculateWithParams(100,30)
sayHello("Mert")
sayHello("Barış")
sayHello("Günay")  


def calculateAndReturn(fiyat,indirim):
    return fiyat-indirim

yeniFiyat = calculateAndReturn(200,50)
print(yeniFiyat + 10)


def calculatePrice(price, discount):
    print(price, discount)

def calculatePriceAndReturn(price, discount):
    return price-discount

print("---------------------------")

#fonk1 = calculatePrice(100,50)
fonk2 = calculatePriceAndReturn(300,100)
#print(f"148.satır: {fonk1 + 100}")
print(f"149.satır: {fonk2 + 100}")

