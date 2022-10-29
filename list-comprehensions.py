from unittest import result


numbers = [x for x in range(10)] 
print(numbers)
print("*"*50) 

numbers = []
for x in range(10):
    numbers.append(x)
print("*"*50) 


#ikisi aynı işlem.
#*************************************
for x in range(10):
    print(x**2)
    
numbers = [x**2 for x in range(10)]
print(numbers)
#*************************************

numbers = [x*x for x in range(10) if x%3 == 0]  #x i 0 dan 9 kadar yazdırıp bunun karesini alıyor ayrıca listeye 3 e tam bölünenleri ekliyor.
print(numbers)

#*************************************

myString = "merhaba"
myList = []
for letter in myString:
    myList.append(letter)
print(myList)

#*************************************

myList = [letter for letter in myString]
print(myList)

#*************************************

result = []

for x in range(3):
    for y in range(3):
        result.append((x,y))

print (result)

numbers = [(x,y,z) for x in range(3) for y in range(3) for z in range(3) ]
print(numbers)