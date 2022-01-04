'''
Szavak.
A program kérjen be két szót a felhasználótól, majd írja ki, hogy melyik a hosszabb! 
A program üzeneteinek megfogalmazásában kövesse az alábbi mintát:
-----
Adj meg egy szót! kelkáposzta
Adj meg egy másik szót! kisegér
A hosszabb szó: kelkáposzta
---- 
Adj meg egy szót! kelkáposzta
Adj meg egy másik szót! káposztafej
A két szó egyforma hosszú.
----- 
Adj meg egy szót! árvíztűrő
Adj meg egy másik szót! tükörfúrógép
A hosszabb szó: tükörfúrógép
'''
szo1 = input("Adjon meg egy szót!")
szo2 = input("Adjon meg egy másik szót!")
if len(szo1) > len(szo2):
    print(szo1)
elif len(szo1) < len(szo2):
    print(szo2)
elif len(szo1) == len(szo2):
    print("A két szó egyforma hosszú!")