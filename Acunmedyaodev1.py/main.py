#video1

print("Acunmedya Akademi")
baslik = "Taşıt Kredisi"
print(baslik)
# string => metinsel ifade
baslik = "İhtiyaç Kredisi"
print(baslik)

# int, integer => Tam Sayı
vade = 36
ekVade = 6
vade2 = "36"

#float, decimal, double
aylikOdeme = 200.50

# bool, boolean => True veya False
yuseklisteMi = False

# Matematiksel Operatörler

# + 

print(5+5)
print(vade+12)
print(vade+ekVade)
print(36+6)

# -

print(5-5)
print(vade-12)
print(vade-ekVade)
print(36-6)

# /

print(5/5)
print(vade/2)
print(vade/ekVade)
print(10/2)

yeniVade = vade / 2
fiyat = 100
indirimliFiyat = fiyat - 20

print(yeniVade)
print(indirimliFiyat)


# % => mod operatör
print(10%2)
print(vade%5)
print(vade%ekVade)
print(30%10)


#mantıksal operatörler

print(1==1)
print(1==2)

print(1>2)
print(3>1)
print(1>1)
print(1>=1)

print(1<2)
print(3<1)
print(1<1)
print(1<=1)

print(1 != 1)
print(1 != 2)


# or and

# or => veya

print(1>2 or 5>2)
print(1>2 and 5>2)
print(1>2 or 5>2 and 3>2)
print(True and False)
print(False and False)
print(True or False)

print(1>2 and 5>2 and 3>2)


# Karar Yapıları 
# if else

sayi1 = 10
sayi2 = 20

if sayi1 < sayi2:
    print("Sayı 1 Sayı 2 den küçüktür")
# Eğer if Bloğuna girmez ise
elif sayi1 == sayi2:
    print("iki sayı eşittir")
else:
    print("Sayı 1 Sayı 2 den büyüktür")    
print("Burası if Bloğunun Dışıdır.")  
 

