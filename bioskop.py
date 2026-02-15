usia = int(input('masukkan usia: '))
hari = input('masukkan hari: ')
member = input('apakah kamu member (y/n): ')

harga_dasar = 50000

if hari == 'sabtu' or hari == 'minggu':
  harga_dasar += 15000

diskon_usia = 0
if usia < 12:
  diskon_usia = 0.2
elif usia > 60:
  diskon_usia = 0.3
else:
  diskon_usia = 0

harga_usia = harga_dasar - (harga_dasar * diskon_usia)

if member == 'y':
  harga_usia -= 5000

if harga_usia < 0:
  harga_usia = 0

harga_usia
