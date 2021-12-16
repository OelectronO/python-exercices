
valeur=[0,0,0,0,0,0,0]
boucle=5
list = 0

for i in range(boucle) :
    list = i+1
    valeur[int(i)] = input("entre la note "+str(int(list))+":")

    if int(valeur[i])>=int(20) :
        valeur[i]=0
        i=int(i)-1
        print("test"+str(i))
        print("Rentre une nouvelle note valide !")
        



print((int(valeur[0])+int(valeur[1])+int(valeur[2])+int(valeur[3])+int(valeur[4]))/int(boucle))