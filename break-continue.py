import re
from unittest import result


name = "İsmail Can"
print("*"*50)
for letter in name :
    if letter == "a":
        break #break komudu koşul sağlandığı anda döngüyü bitirir.
    print(letter) 
    
print("*"*50)    
 
for letter in name :
    if letter == "s":
        continue #continue komutu koşul sağlandığında sağlanan koşulu atlar ve devam eder.
    print(letter)
    
print("*"*50)   

x=0
while x<5:
    x+=1
    if x == 2:
        break
    print(x)
     
print("*"*50) 

y=0
while y<5:
    y+=1
    if y == 2:
        continue
    print(y)
    
print("*"*50) 
    
x = 0
result = 0
while x <= 100 :
    x+=1
    if x % 2 ==0:
        continue
    result += x
print(result)