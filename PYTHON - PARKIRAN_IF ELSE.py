kendaraan = input('Masukkan kendaraan: ')
jam = int(input('Masukkan jam: '))

tarif = 0

if kendaraan == 'motor':
  tarif = 2000
elif kendaraan == 'mobil':
  tarif = 5000

tarif_total = tarif * jam

if tarif_total > 30000:
  tarif_total = 30000

if jam > 24:
  tarif_total_denda = tarif_total + 10000
else:
  tarif_total_denda = tarif_total

print(f'Tarif yang harus anda bayarkan adalah {tarif_total}')
print(f'Tarif + denda yang harus anda bayarkan adalah {tarif_total_denda}')
