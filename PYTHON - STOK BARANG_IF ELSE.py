barang = {
    "Kaos": 50,
    "Kemeja": 20,
    "Celana Jeans": 5,
    "Jaket": 12,
}

while True:
  print("1. Lihat Stok")
  print("2. Update Stok")
  print("3. Restock")
  print("4. Peringatan")

  pilih = (input('Masukkan pilihan: ')).title()

  if pilih == 'Selesai':
    print('Terimakasih')
    break
  
  pilihan = int(pilih)

  if pilihan == 1:
    for pakaian, stok in barang.items():
      print(f'- Stok {pakaian} adalah {stok}')

  elif pilihan == 2:
    pakaian = input('Masukkan pakaian yang terjual: ')
    if pakaian in barang:
      jumlah = int(input('Berapa banyak barang yang terjual? '))
      if barang[pakaian] >= jumlah:
        barang[pakaian] -= jumlah
        print(f'Stok {pakaian} telah diperbarui menjadi {barang[pakaian]}')
      else:
        print('Barang tidak ditemukan')

  elif pilihan == 3:
    stok_baru = input('Masukkan barang yang ingin di restok: ')
    if stok_baru in barang:
      jumlah = int(input('Masukkan berapa banyak barang yang ingin di tambahkan: '))
      barang[stok_baru] += jumlah
    else:
      print('Barang tidak ada di sistem')

  elif pilihan == 4:
    for stok in barang:
      if barang[stok] < 15:
        print(f'{stok} hampir Habis')
      else:
        print(f'{stok} masih banyak')