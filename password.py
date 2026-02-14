#password
#ilangin spasi
password = input('Masukkan password: ').replace(" ", "")

panjang = len(password) >= 8
ada_angka = False
ada_kapital = False

for karakter in password:
  if karakter.isdigit():
    ada_angka = True
  elif karakter.isupper():
    ada_kapital = True
bintang = len(password)* "*"
if panjang and ada_angka and ada_kapital:
  print(f'password valid {bintang}')
else:
  print('password tidak valid')