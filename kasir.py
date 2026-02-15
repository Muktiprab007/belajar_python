daftar_belanja = {}

while True:
  nama_barang = input('Masukkan nama barang: ')

  if nama_barang == 'selesai':
    break

  if nama_barang in daftar_belanja:
    harga_tercatat = daftar_belanja[nama_barang]['harga']
    print(f"Barang ditemukan! Harga: Rp{harga_tercatat}")

    jumlah_barang = int(input('Masukkan Jumlah barang: '))
    daftar_belanja[nama_barang]['jumlah'] += jumlah_barang
  else:
    harga_barang = int(input('Masukkan Harga barang: '))
    jumlah_barang = int(input('Masukkan Jumlah barang: '))
    daftar_belanja[nama_barang] = {'harga' : harga_barang, 'jumlah' : jumlah_barang}

total_seluruhnya = 0
for barang, data in daftar_belanja.items():
  price = data['harga']
  stok = data['jumlah']

  total_harga = price * stok
  total_seluruhnya += total_harga

  print(f"{barang.capitalize()}: {stok} pcs x Rp{price} = Rp{total_harga}")

print(total_seluruhnya)