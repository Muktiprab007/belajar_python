denah = [
    [1, 0, 1], # Baris 0
    [0, 0, 0], # Baris 1
    [1, 1, 0]  # Baris 2
]

baris = int(input('Masukkan Baris(0-2): '))
kursi = int(input('Masukkan Kursi(0-2): '))

if denah[baris][kursi] == 0:
  denah[baris][kursi] = 1
else:
  print('Maaf Kursi Sudah Penuh')

#denah kursi terbaru
for b in denah:
  print(b)

kosong = 0
for b in denah:
  for k in b:
    if k == 0:
      kosong += 1

print(f"\nSisa kursi kosong: {kosong}")

