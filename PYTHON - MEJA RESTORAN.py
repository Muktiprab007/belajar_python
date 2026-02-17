meja_restoran = {
    1: {"kapasitas": 2, "status": "tersedia"},
    2: {"kapasitas": 4, "status": "tersedia"},
    3: {"kapasitas": 4, "status": "tersedia"},
    4: {"kapasitas": 8, "status": "tersedia"},
    5: {"kapasitas": 10, "status": "tersedia"}
}

while True:
  orang = input('masukkan jumlah orang: ')

  if orang.lower() == 'keluar':
    break

  jumlah_orang = int(orang)
  tersedia = False

  for nomor, info in meja_restoran.items():
    if info['status'] == 'tersedia' and info['kapasitas'] >= jumlah_orang:
      info['status'] = 'dipesan'
      tersedia = True
      print(f'Meja nomor {nomor} berhasil dipesan untuk {jumlah_orang} orang.')
      break

  if not tersedia:
    print('Maaf, tidak ada meja yang sesuai untuk jumlah orang tersebut.')
