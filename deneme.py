kilo = int(input("Kilonuzu giriniz: "))
boy = int(input("Boyunuzu giriniz: "))
boy = boy/100
bki = kilo/boy**2
print(bki)

if bki < 19:
    print("zayıf")
elif ( bki>=19 ) + ( bki<=24 ):
    print("normal")
else:
    print("kilolu")