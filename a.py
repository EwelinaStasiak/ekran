import max7119

#inicjalizacja
max7119.write(0x09, 0)
max7119.write(0x0A, 3)
max7119.write(0x0B, 7)
max7119.write(0x0C, 1)

#wczytywanie pliku
lista = []
plik = open('obraz.txt', 'r')
for linia in plik.readlines():
   string =linia.replace('X', '1')
   lista.append(string.strip())
print(lista)

for i in range(len(lista)):
   liczba_1 = int(lista[i], 2)
   liczba_2 = i + 1
   print(liczba_1, liczba_2)
   max7119.write(liczba_2, liczba_1)





#00000000
#0XXXXXX0
#0X000000
#0X000000
#0XXXXX00
#0X000000
#0XXXXXX0
#00000000

