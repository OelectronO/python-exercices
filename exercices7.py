
reset = True
while(reset == True) :

    first_number = input("premier nombre")
    second_number = input("deuxieme nombre")

    operation = input("une operation")

    if(operation == "+") :
        calcul = int(first_number) + int(second_number)
    elif(operation == "-") :
        calcul = int(first_number) - int(second_number)
    elif(operation == "/") :
        calcul = int(first_number) / int(second_number)
    elif(operation == "*") :
        calcul = int(first_number) * int(second_number)
    else :
        print("tu as choisi un mauvais operateur ! recommence avec '+' ou '-' ou '/' ou '*' ")


    print(calcul)

    reset = bool(input("recommencé"))

    if(reset == "non") :
        reset = False