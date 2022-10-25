# set tanımlaması için süslü parantez arasına yazılır.
#bu liste aynı sayıları yazdırmaz.
#lstede bulunan bir eleman tekrar eklenemez.


from asyncio import futures


fruits = { "orange" , "apple", "banana","banana"}

# print(fruits[0]) indekslenemez

for x in fruits :
    print(x) 
fruits.add("cherry")
fruits.update(["mango", "grape" , "apple"])
#ekleme araçları

fruits.remove("mango")
fruits.discard("apple")
fruits.pop() #rasgele elemanı siler.
fruits.clear() #tüm elemanları siler.
#silme araçları




number= [1,5,6,2,5,6,2,5,1,5,12,4,5,2,6,5,3]
print(number)
print(set(number)) #tekrarlayan elemanları siler.