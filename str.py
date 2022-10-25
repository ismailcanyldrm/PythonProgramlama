name = "İsmail Can "
surname = "Yıldırım "
age = 22

cv = "Name : " + name + "\nSurname : " + surname + "\nAge : " + str(age)
print("******************")
print(cv) #cv ini içini yazdırır
print("******************")
print(len(cv)) #cv nin karakter uzunluğunu yazdırır
print("******************")
print(cv[-1]) # cvnin son karakterini yazdırır
print("******************")
print(cv[3:5]) # cv nin 3 den 5 e kadar olan karakterlerini yazzdırır
print("******************")
print (cv[9:]) # 9. karakterden sonrasını yazdırır
print("******************")
print(cv[:9]) # 9. karaktere kadar yazdırır
print("******************")
print(cv[0:47:2]) # 0 dan 47 ye kadar 2 şer atlayarak yazdırır
print("******************")
print(cv[0:47:1]) # 0 dan 47 ye birer birer yazdırır
print("******************")
print(cv[::]) # tüm karakterleri yazdırır
print("******************")
print(cv[::-1]) # tüm karakterleri tersine çevirir
print("******************")


