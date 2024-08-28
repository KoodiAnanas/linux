import random

# Määritellään korttipakka
maat = ['Hertta', 'Ruutu', 'Risti', 'Pata']
arvot = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# Luodaan korttipakka
korttipakka = [arvo + ' ' + maa for maa in maat for arvo in arvot]

# Sekoitetaan korttipakka
random.shuffle(korttipakka)

# Jaetaan kortit kahdelle pelaajalle
pelaaja1 = korttipakka[:26]
pelaaja2 = korttipakka[26:]

# Tulostetaan pelaajien kortit
print("Pelaaja 1:n kortit:")
print(pelaaja1)
print("\nPelaaja 2:n kortit:")
print(pelaaja2)