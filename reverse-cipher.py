# reverse-cipher.py
#==================
wiadomosc= 'To jest tekst do zaszyfrowania'
print(wiadomosc)
zaszyfrowany = ''
i = len(wiadomosc) -1

while i >= 0:
	zaszyfrowany = zaszyfrowany + wiadomosc[i]
	i = i-1
print("Zaszyfrowana wiadomość to:", zaszyfrowany)

#  A teraz odwrócimy tekst
#==========================
wiadomosc = zaszyfrowany
zaszyfrowany = ''
i = len(wiadomosc) -1

while i >= 0:
	zaszyfrowany = zaszyfrowany + wiadomosc[i]
	i = i-1
print("Odszyfrowana wiadomość to:", zaszyfrowany)
