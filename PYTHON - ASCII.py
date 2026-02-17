teks = input('Masukkan pesan rahasia: ')
lompat = int(input('Jumlah geseran (angka): '))
hasil_enkripsi = ''
for karakter in teks:
  if karakter.isalpha():
    kode_ascii = ord(karakter)

    kode_baru = kode_ascii + lompat

    huruf_baru = chr(kode_baru)

    hasil_enkripsi += huruf_baru
  else:
    hasil_enkripsi += karakter

print(f'\nPesan terenskripsi: {hasil_enkripsi}')
