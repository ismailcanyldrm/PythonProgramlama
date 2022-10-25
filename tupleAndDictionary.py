#TUPLE

#tuple yani demet veri tipleri listenin içeriğini değiştiremeyiz silemeyiz ekleyemeyiz
#kare parantez yerine normal parantez ile gösterilir.
from pydoc import plain
from tkinter import N


tuple = ("damla","ayşe","demet")

#DİCTİONARY

# key - value
# 41 - kocaeli
#güncelleme yapabiliyoruz.

plakalar= { "istanbul" : 34 , "ankara" : "06" }

print(plakalar["ankara"])

Öğrenciler = {
    "1" : {
        "Ad" : "İsmail Can",
        "Soyad" : "Yıldırım",
        "No" : "180603038" 
    }

}
number = input("öğrenci sırası : ")
name = input("öğrenci adı : ")
surname = input("öğrenci soyadı : ")
no = input("öğrenc no : ")

Öğrenciler[number] = {
        "Ad" : name,
        "Soyad" : surname,
        "No" : no
}
#bu üsteki işlem ile listeye veri ekleyebiliyoruz

Öğrenciler.update({
    number: {
    "Ad" : name,
    "Soyad" : surname,
    "No" : no,
    }
})
##bu üsteki işlem ile listeye veri ekleyebiliyoruz sadece daha fomksiyonel kullanılıyor.
print("*"*50)

x = input("öğrenci sırası : ")
ogrenci = Öğrenciler[x]
print(ogrenci)

print(f"Aradığınız {x} sıralı öğrenci adı : {ogrenci['Ad']} soyadı : {ogrenci['Soyad']} ve numarası ise {ogrenci['No']}")
