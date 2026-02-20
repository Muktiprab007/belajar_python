n = int(input('Tampilkan angka prima sampai angka: '))

prima = []

for angka in range(2, n + 1):
  is_prima = True
  for pembagi in range(2, angka):
    if angka % pembagi == 0:
      is_prima = False
  
  if is_prima:
    prima.append(angka)

print(prima)
print(pembagi)
