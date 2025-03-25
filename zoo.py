def pridej(zvire, pocet):
    global tygri
    global lvy
    global opice
    if zvire == "tygri":
        tygri += pocet
    elif zvire == "lvy":
        lvy += pocet
    elif zvire == "opice":
        opice += pocet
    else:
        print("Neco si zadal špatně")

tygri = 0
lvy = 0
opice = 0

opakovat = "ano"

while(opakovat=="ano"):

    print("Vyberte jednu z akcí(pište pouze číslo): ")
    print("1. přidat zvíře")
    print("2. odebrat zvíře")
    print("3. vypsat seznam zvířat")

    cislo = int(input())
    
    if cislo==1:
        zvire = input("Zadejte zvířata která chcete přidat(tygri,lvy,opice)")
        pocet = int(input("Zadejte počet těchto zvířat"))
        pridej(zvire,pocet)
    elif cislo==2:
        zvire = input("Zadejte zvířata která chcete přidat(tygri,lvy,opice)")
        pocet = int(input("Zadejte počet těchto zvířat"))
        odeber(zvire,pocet)
    elif cislo==3:
        vypis()

    opakovat = input("Chcete opakovat program?(ano/ne)")
