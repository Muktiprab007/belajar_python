menu = {
    "Nasi Goreng": 15000,
    "Mie Ayam": 12000,
    "Es Teh": 5000,
    "Somay": 10000,
    "Nasi Uduk": 10000,
    "Mie Tek-Tek": 12000,
    "Pecel" : 12000,
    "Marimas": 3000
}

total_belanja = 0

for makanan, harga in menu.items():
  print(f'- {makanan} dengan harga Rp{harga}')

while True:
  pilih = input('Masukkan makanan pilihan atau selesai: ').title()

  if pilih == 'Selesai':
    break
  
  if pilih in menu:
    harga = menu[pilih]
    total_belanja += harga
  else:
    print('Pilihan Tidak Ada di Menu')

total_bayar = 0
diskon = 0
if total_belanja > 50000:
  diskon = 0.1 * total_belanja

total_bayar = total_belanja - (total_belanja * 0.1)

print(f'Diskon yang didapatkan adalah {diskon}')
print(f'Harga yang harus dibayarkan adalah Rp{total_bayar}')