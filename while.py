# 1 den 100 kadar sayıları yazdır.
 x = 0
 while x < 1000 :
     x+=1
     print(x)


 name = ""

 while not name:
     name = input("isminizi giriniz : ")
    
 print(f"merhaba {name}")


sayilar = [1,3,5,7,9,12,19,21]
x=0
while (x<len(sayilar)):
    
    print(sayilar[x])
    x+=1
    
    
x = int(input("Başlangıç Değeri Girin : "))
y = int(input("Bitiş Değeri Girin : "))
while (x<=y):
    print(x)
    x+=1
    
numbers= []
i=0
while i<5:
    sayi=int(input("sayi : "))
    numbers.append(sayi)
    i+=1
numbers.sort()
print(numbers)