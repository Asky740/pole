zbozi = ["CPU", "GPU", "RAM", "HDD", "SSD", "Motherboard", "Chlazní", "Zdroj", "Case"]
kosik = []

def vypis_pole(a):
    for x in range(len(a)):
        print(f"{x+1}. {a[x]}")

def je_cislo(b):
    for i in range(len(b)):
        if b[i].isdigit() != True:
            return False
    return True

while len(zbozi) > 0:
    print(" ")
    print("\033[1mNabídka zboží:\033[0m")
    vypis_pole(zbozi)
    print(" ")
    print("\033[1mStav Vašeho košíku:\033[0m")
    vypis_pole(kosik)
    print(" ")
    print("-------------------------------------------------")
    print(" ")

    pridani = input("Zadejte zboží, které chcete přidat: ")

    if je_cislo(pridani) == True:
        pridani = int(pridani)
        kosik.append(pridani)
        zbozi.pop(pridani)

    elif je_cislo(pridani) == False:
        kosik.append(pridani)
        zbozi.remove(pridani)


    elif je_cislo(pridani):
        print("wtf")

    print(" ")
    print("                \033[1mZboží přidáno!\033[0m")
    print(" ")
    print("-------------------------------------------------")