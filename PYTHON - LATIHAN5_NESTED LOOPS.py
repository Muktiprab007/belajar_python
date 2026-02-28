monitor_rs = [
    [1, 0, 1], # Lantai 1
    [0, 1, 0], # Lantai 2
    [1, 1, 0]  # Lantai 3
]

lantai = int(input('Masukkan lantai yang diinginkan: '))
kamar = int(input('Masukkan kamar yang diinginkan: '))

if monitor_rs[lantai][kamar] == 0:
  monitor_rs[lantai][kamar] =  1
else:
  print('Maaf Kamar sudah penuh')

for m in monitor_rs:
  print(m)

kamar_kosong = 0
for m in monitor_rs:
  for k in m:
    if k == 0:
      kamar_kosong += 1

print(f'Kamar kosong yang tersedia adalah: {kamar_kosong}')