message = "Seni araken kendimi kaybetmekten yoruldum Bulduğumu zannettiğimde kendimden ayrı düştüm"
websitesi = "https://www.google.com.tr"

#message=message.lower() #listedeki tüm karakterleri küçük harf yapar

#message=message.upper() #listedeki tüm karakterleri büyük harf yapar

#message=message.title()  #listedeki tüm kelimelerin ilk harfini büyük harf yapar

#message=message.capitalize()   #sadece baş harfi büyük yapar

#message=message.strip()   #cumlelerin başındaki ve sonundaki boşluğu siler.

#message=message.lstrip()   #cumlelerin solundaki boşluğu siler.

#message=message.rstrip()   #cumlelerin sağındaki boşluğu siler.

#message = websitesi.strip("htp:/.coswtrm") # parantez içindeki sözcükleri sağdan soldan iki köşeden olarak parantezin içindekini siler. sağ ve sol için lstrip veya rstrip kullanılır.

#message = websitesi.count("o") # parantez içindeki karakterin kaç tane olduğu sayısını yazdırır.

#message = websitesi.count("o",0,20) # parantez içindeki karakterin 0 ile 20 haneleri arasında kaç tane olduğu sayısını yazdırır.

#message=message.split()  #boşlukları virgül ile ayırır.

#message=message.split(.)  #noktadan itibaren virgül ile ayırır.

#message = "*".join(message) #parçaladığımız yerleri * ile ayırmaya yarar.

#index = message.find("ayrı") #parantez içindeki kelimenin listede olup olmadığını kontrol eder. varsa başladığı index sayısını yoksa -1 değeri çevirir.

#isFound = message.startswith("S") # S ile başlıyorsa true değeri döndürüyor, eğer başka bir değerle başlıyorsa false döndürür.

#isFound = message.endswith("m") # m ile bitiyorsa true değeri döndürüyor, eğer başka bir değerle başlıyorsa false döndürür.

#message = message.replace(" ","*") # boşluk yerıne * ifadesini koyar bu ç yerine c gibi de kullanılabilir.

#message = message.center(100,"*") #100 hane içinde ortalama ve tamamlamayı * ile yap demek yerine boşluk vs gelebilir.

#message = message.isalpha()  # message içeriği alhabetik mi sorunu cevaplar.


#print(isFound)
#print(index)
print(type(message))