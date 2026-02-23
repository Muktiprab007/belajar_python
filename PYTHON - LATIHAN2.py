kiriman = ["Kaos", "Celana", "Kaos", "Topi", "Celana", "Kaos", "Jaket"]

rekap_barang = {}

for barang in kiriman:
  if barang in rekap_barang:
    rekap_barang[barang] += 1
  else:
    rekap_barang[barang] = 1

for nama, jumlah in rekap_barang.items():
  print(f'- {nama} dengan {jumlah} pcs')