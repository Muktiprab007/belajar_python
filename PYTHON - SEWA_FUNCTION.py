def hitung_jam(jam, menit, member):
  if menit > 10:
    jam_bayar = jam + 1
  else:
    jam_bayar = jam
  
  total_harga = jam_bayar * 15000

  if member == 'y':
    total_harga -= 5000
  
  return f'total Biaya: Rp{total_harga}'

jam = int(input('Masukkan berapa jam: '))
menit = int(input('Masukkan berapa menit: '))
member = input('Apakah member (y/n): ')

hasil = hitung_jam(jam, menit, member)
print(hasil)