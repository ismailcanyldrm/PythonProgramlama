# Listeler her türlü veriyi tutabilirler.
# listeler stringler gibi birbirleri ile toplanabilirler.

yourList = [56,"ismail", True, 125.64 ]
myList= ["a","b","c"]

listeElemanSayisi = len(myList) # len komutu bize listenin uzunluğunu verir.

result = 56 in yourList #56 rakamı listenin içinde varmı true - false

#del myList[-1] # listenin son elemanını siler parantez içine istediğimiz yeri yazdırıp silebiliriz.


print(min(myList)) #listedeki sayı veya harf olarak en küçüğü verir
print(max(myList)) #listedeki sayı veya harf olarak en büyüğü verir


myList.append("d") #listeye yazdığımız veriyi listenin sonuna ekler.
yourList.append("karakter") #listeye yazdığımız veriyi listenin sonuna ekler.
myList.insert(1,"yeni")  #listenin istediğimiz konumuna eklemeyi sağlar.
yourList.insert(-1,"trigonometri") #listenin istediğimiz konumuna eklemeyi sağlar.

myList.pop() #listenin sonundaki şeyi kaldırır
myList.pop(0) #listeden 0. indexdeki elemenı siler
yourList.pop(-1) #listeden sondan önceki elemanı siler
myList.remove("b") # ismini sayısını yazdığımız elemanı siler
myList.sort() #listeyi büyükten küçüğe a dan z ye listeler
myList.reverse() #listeyi tersine cevirir
myList.clear() #listedeki tüm herşeyi siler 

print(myList.count("d")) 

print(result)
print(myList)
print(yourList)
print(listeElemanSayisi)