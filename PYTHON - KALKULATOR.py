while True:
  print('Pilih Operasi')
  print('1. Perkalian')
  print('2. Pembagian')
  print('3. Penambahan')
  print('4. Pengurangan')
  print('5. Pangkat')
  print('6. Rata-rata')
  print('0. Keluar')

  pilihan = int(input('Masukkan Pilihan: '))

  list_angka = []

  if pilihan == 0:
    print('Terimakasih Sudah Menggunakan Kalkulator Saya')
    break

  if pilihan not in [1, 2, 3, 4, 5, 6]:
    print('Pilih Operasi Sesuai Opsi: ')
    continue

  jumlah = int(input('Masukkan Berapa Kali Ingin Memasukkan Angka: '))

  for i in range(jumlah):
      angka = int(input(f'Masukkan angka ke-{i+1}: '))
      list_angka.append(angka)

  if pilihan == 1:
    hasil = 0
    for angka in list_angka:
      hasil *= angka
    print(f'Hasil Perkalian: {hasil}')

  elif pilihan == 2:
    hasil = list_angka[0]
    error = False
    for i in range(1, len(list_angka)):
      if angka == 0:
        error = True
        break
      hasil /= list_angka[i]

    if not error:
      print(f'Hasil Pembagian: {hasil}')

  elif pilihan == 3:
    hasil = 0
    for angka in list_angka:
      hasil += angka
    print(f'Hasil Penjumlahan: {hasil}')

  elif pilihan == 4:
    hasil = list_angka[0]
    for i in range(1, len(list_angka)):
      hasil -= list_angka[i]
    print(f'Hasil Pengurangan: {hasil}')

  elif pilihan == 5:
    hasil = list_angka[0]
    for i in range(1, len(list_angka)):
      hasil ** list_angka[i]
    print(f'Hasil pemangkatan: {hasil}')

  elif pilihan == 6:
    total = 0
    for i in list_angka:
      total += list_angka[i]
      mean = total / len(list_angka[i])
    print(f'Hasil Rata-rata')
    
  while True:
    lanjut = input('Apakah mau lanjut (y/n): ')
    if lanjut.lower() == 'y':
        break
    elif lanjut.lower() == 'n':
        print('Terimakasih sudah menggunakan kalkulator saya')
        break
    else:
        print('Input Tidak Valid')
