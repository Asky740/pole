cislo = int(1) #tohle je datovy typ celeho cisla
cislo_flaot = float(3.23) #tohle je cislo s desetinou carkou
text = str("String je sada znaků, napriklad pro text")
Boolean = True #Booleanska hodnota, znaci bud pravdu/nepravdu (True/False)
#datovy typ pole, kde muzeme mit vice prvku
#v poli se zacina na pozici nula, ackoliv je delka pole 6, posledni prvek je na pozici 5
            #0        #1       #2     #3        #4        #5
arrays = ["Ford", "Porsche", "Audi", "BMW", "Mercedes", "Škoda"]

#tohle vypise uplne cele pole vcetne zavorek a uvozovek s carkama
    #print(arrays)

#tohle vypise pouze jeden prvek bez uvozovek, carek a hranatych zavorek, vypise jen Porsche
    #print(arrays[1])

for x in range(6):
    print("#",1+x, arrays[x])