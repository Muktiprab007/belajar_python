#antrean klien
antrean = []
while True:
  print(f"Jumlah antrean saat ini: {len(antrean)} orang")
  print("1. Tambah Pasien")
  print("2. Panggil Pasien")
  print("3. Lihat Antrean")
  print("4. Selesai")
  
  pilihan = int(input('Masukkan Pilihan Anda: '))
  if pilihan == 1:
    nama = input('Masukkan Nama Pasien: ')
    antrean.append(nama)
    print('Berhasil ditambahkan')
  elif pilihan == 2:
    antrean.pop(0)
  elif pilihan == 3:
    if len(antrean) > 0:
      for i in range(len(antrean)):
        print(f'antrean ke-{i + 1} adalah {antrean[i]}')
    else:
      print('Belum ada antrian')
  elif pilihan == 4:
    print('Terima Kasih')
    break
  else:
    print('pilih yang bener dong!!!')