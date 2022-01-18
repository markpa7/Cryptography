###  Szyfr-Cezara2.py z pliku do pliku
###===================================
def szyfruj(tekst, rotacja):
	szyfr = ""
	for i in range(len(tekst)-1):	# odejmuje 1,bo nakońcu jest LF z pliku
		litera = tekst[i]
		#print("litera= ", litera)
		if litera == " ":
			szyfr += " "
		else:
			if (litera.isupper()):
				#print(ord(litera), end=" ")
				szyfr += chr(abs(ord(litera) -65 + rotacja) % 26 + 65)
			else:
				#print(ord(litera), end=" ")
				szyfr += chr(abs(ord(litera) -97 + rotacja) % 26 + 97)
	return szyfr

#wiadomosc = "Taka ABCDE WIADOMOSC"

plik1 = 'do-szyfru.txt'
with open(plik1, "r") as linia_pliku:
	linie = linia_pliku.readlines()

przesuniecie = 3

print("Nasz tekst:  ", linie)
# W jednej lini
czysty_tekst = ''.join([str(i) for i in linie])
# albo w trzech:
#czysty_tekst = ''
#for i in linie:
#	czysty_tekst += str(i)
print("Czysty_tekst: ", czysty_tekst)
szyfr_tekst = szyfruj(czysty_tekst, przesuniecie)
print("\nZaszyfrowane: " + szyfr_tekst)

# Zapis do pliku
plik2 = 'dz-szyfru.txt'
with open(plik2, "w") as linia_pliku:
	linia_pliku.write(szyfr_tekst)
