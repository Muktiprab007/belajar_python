peta = [
    ['S', 'S', 'S'],
    ['S', 'S', 'S'],
    ['S', 'S', 'S']
]

baris = int(input('Masukkan Baris: '))
kolom = int(input('Masukkan Kolom: '))

if peta[baris][kolom] == 'S':
  peta[baris][kolom] = 'X'
else:
  print('Koordinat sudah ditandai')

for b in peta:
  print(b)

kosong = 0
for b in peta:
  for k in b:
    if k == 'S':
      kosong += 1
print(f'Koordinat yang masih belum ditelusuri adalah {kosong}')