kiriman = ["Kaos", "Celana", "Kaos", "Topi", "Celana", "Kaos", "Jaket"]

rekap_barang = {}

for nama in kiriman:
  if nama in rekap_barang:
    rekap_barang[nama] += 1
  else:
    rekap_barang[nama] = 1

for benda, jumlah in rekap_barang.items():
  print(f'- {benda} berjumlah sebanyak {jumlah}')