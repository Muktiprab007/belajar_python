daftar_menu = {
    "Salad": 25000,
    "Smoothie": 30000,
    "Jus Apel": 15000
}

total_harga_menu = 0 

while True:
  pesanan = input('Masukkan Pesanan kamu: ')

  if pesanan == 'selesai':
    break

  if pesanan in daftar_menu:
    total_harga_menu += daftar_menu[pesanan]
  else:
    print('Pesanan Tidak ada di menu')

print(total_harga_menu)