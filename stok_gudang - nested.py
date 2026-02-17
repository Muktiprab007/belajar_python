stok_gudang = [
    [10, 5, 8, 10, 5],
    [2, 0, 15, 6, 2],
    [7, 12, 4, 8, 0]
]
nama_produk = ["HP", "Laptop", "Tablet", 'PS', 'Nintendo Switch']
total_semua = 0

for i in range(len(stok_gudang)):
  print(f'Cabang ke-{i+1}')
  total_cabang = 0

  for j in range(len(stok_gudang[i])):
    jumlah = stok_gudang[i][j]
    nama = nama_produk[j]

    print(f"- {nama}: {jumlah} unit")
    if jumlah == 0:
      print(f'PERINGATAN: {nama} di Cabang {i+1} Habis!')

    total_cabang += jumlah
    total_semua += jumlah
  print(f"Total Stok Cabang {i+1}: {total_cabang} unit")

for j in range(len(nama_produk)):
  total_per_barang = 0
  produk = nama_produk[j]

  for i in range(len(stok_gudang)):
    total_per_barang += stok_gudang[i][j]

    print(f"Total stok {produk} di semua cabang: {total_per_barang} unit")

print(f"Total semua stok: {total_per_barang} unit")