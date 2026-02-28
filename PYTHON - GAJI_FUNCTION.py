def hitung_gaji(jumlah_kata, kualitas = "Standar"):
  gaji_awal = 500 * jumlah_kata

  kualitas = kualitas.strip().title()

  if kualitas == "Bagus":
    gaji = gaji_awal + 1.2
  elif kualitas == "Sangat Bagus":
    gaji = gaji_awal + 1.5
  
  gaji_akhir = gaji - 5000

  if gaji_akhir < 0:
    return 0
  
  return int(gaji_akhir)
  
kata = int(input('Masukkan jumlah kata: '))
level = input('Masukkan level: ')

total_diterima = hitung_gaji(kata, level)
print(f"Total gaji yang ditransfer: Rp{total_diterima}")