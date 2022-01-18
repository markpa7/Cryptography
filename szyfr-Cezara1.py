###  Szyfr-Cezara1.py
###==================
def szyfruj(tekst, rotacja):
	szyfr = ""
	for i in range(len(tekst)):
		litera = tekst[i]
		if litera == " ":
			szyfr += " "
		else:
			if (litera.isupper()):
				print(ord(litera), end=" ")
				szyfr += chr(abs(ord(litera) -65 + rotacja) % 26 + 65)
			else:
				print(ord(litera), end=" ")
				szyfr += chr(abs(ord(litera) -97 + rotacja) % 26 + 97)
	return szyfr

wiadomosc = "Taka ABCDE WIADOMOSC"
przesuniecie = 3

print("Nasz tekst:  ", wiadomosc)
print("\nZaszyfrowane: " + szyfruj(wiadomosc, przesuniecie))
