# Créé par mathys.boutry, le 02-12-2021 en Python 3.7

classe = input("les classes :\n\n-1- Guerrier,  14 Vie, 5 Domage, 6 Defense\n\n-2- Archer,  7 Vie, 8 Domage, 3 Defense\n\n-3- Mage,  5 Vie, 12 Domage, 3 Defense")

if(classe == 3) :
    print("tu as choisi le Mage")
elif(classe == 2) :
    print("tu as choisi l'archer")
else :
    print("tu as choisi le Guerrier")