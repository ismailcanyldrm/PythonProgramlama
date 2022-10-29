import random 

x = random.randint(0,100)
print(x)
print("0 ile 100 arasında bir sayı tuttum hadi onu bil")

i = 0
while i<6:
    i+=1
    y = int(input("Tahmini Alalım : "))
    if x == y:
        print(f"Bravo bildin. Tuttuğum sayı : {x}")
    elif x > y : 
        print("Sayıyı biraz arttırmayı dene")
    elif x < y :
        print("sayıyı biraz azaltmayı dene ")
    