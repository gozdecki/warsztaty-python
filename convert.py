kol1 = []
kol2 = []

for linia in open('reference.csv'):
   data = linia.split(',')
   kol1.append(float( data[0]))
   kol2.append(float( data[1]))

liczba_lini = len(kol1)

plik = open("wynik.csv","w")
plik.write(str(liczba_lini)+'\n')

for indeks in range(liczba_lini):
   linia = '{:.3e};{:.3f}\n'.format(kol1[indeks], kol2[indeks])
   plik.write(linia)

plik.close()
