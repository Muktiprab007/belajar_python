nama_buku = input('Masukkan Nama Buku: ')
durasi_pinjam = int(input('Mau Berapa Hari Pinjam Buku?: '))
batas_pinjam = 7
denda = 2000
terlambat = durasi_pinjam - batas_pinjam
status = 'Aktif'

if durasi_pinjam <= 7:
  denda = 0
else:
  denda = denda * terlambat

if denda > 20000:
  print('you are banned')
else:
  print(status)

print(denda)