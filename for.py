# deneme = {"k" : 1 , "k2" : 2} 

# for value , key in deneme.items ():
#     print(key)
    

sayilar = [1,3,5,7,9,12,19,21]


for i in sayilar :
    if (i % 3 == 0):
        print(i)
        
        
print("*"*50)

a = 0
for s in sayilar :
    a += s  
print(a)

print("*"*50)

for tek in sayilar :
    if (not tek%2 == 0):
        b = tek**2
        print(b)
        
print("*"*50)


sehirler = ["kocaeli","istanbul","ankara","izmir","rize"]

for sehir in sehirler :
    if sehir.count("")<=6 :
        print(sehir)
        
print("*"*50)

for sehir in sehirler : 
    if len(sehir)<=5:
        print(sehir)
print("*"*50)   

urunler = [
    {'name' : 'samsung s6 ', 'price' : '3000'},
    {'name' : 'samsung s7 ', 'price' : '4000'},
    {'name' : 'samsung s8 ', 'price' : '5000'},
    {'name' : 'samsung s9 ', 'price' : '6000'},
    {'name' : 'samsung s10 ', 'price' : '7000'}   
]
x = 0
for sup in urunler :
    print(sup['price'])
    x += int(sup['price'])
print(x)
       
       
print("*"*50)   

for sira in urunler :
    if int(sira['price'])<= 5000 :
        
        print(sira['price'],sira['name'])