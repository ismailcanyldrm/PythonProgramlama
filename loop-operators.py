print("RANGE")
print("*"*50) 
for item in range(10):#0 dan 9 a kadar 10 tane sayar
    print(item)

print("*"*50) 

for item in range(10,100):# 10 dan 100 e kadar yazdırır 100 dahil değil.
    print(item)
    
print("*"*50) 

for item in range(10,100,5):# 10 dan 100 e kadar yazdırır 100 dahil değil ve 5 er 5 er aralıkla.
    print(item)
    
print("*"*50) 

mylst = list(range(1,99,2))
print(mylst)

print("*"*50) 
print("Enumerate")

index = 0
greeting = "hello dünya"

for letter in greeting :
    print(f"index : {index} letter : {greeting[index]}")
    index += 1
    
print("*"*50)     


greeting = "ismailcan"     
for index,item in enumerate(greeting) :
    print(f"index : {index} letter : {item}")


print("*"*50)    

print("ZİP")

list1 = [1,2,3,4,5]  
list2 = ["a","b","c","d","e"]  

print(list(zip(list1,list2)))
