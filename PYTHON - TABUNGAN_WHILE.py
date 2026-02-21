target = 100000

tabungan = []

while True:
  tabungan_harian = int(input('Masukkan Tabungan Hari Ini: '))
  tabungan.append(tabungan_harian)

  total_tabungan = sum(tabungan)
  if total_tabungan >= target:
    print(f'Target Terpenuhi {total_tabungan}')
    break
  else:
    print('Target belum tercapai')

  print(f'Tabungan sementara adalah {total_tabungan}')