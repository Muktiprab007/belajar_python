def hitung_biaya_intl(durasi_input):
  durasi = durasi_input
  harga_dasar = 2000
  harga = (durasi * harga_dasar) + 5000

  if durasi > 30:
    total_biaya = harga + (harga * 0.1)
  elif 10 <= durasi <= 30:
    total_biaya = harga + (harga * 0.05)
  else:
    total_biaya = harga
  
  return f'Total Biaya yang Harus dibayarkan adalah {total_biaya}'

durasi = int(input('Masukkan durasi: '))
hasil = hitung_biaya_intl(durasi)
print(hasil)
