def cek_promo(kode):
  kode = kode.strip().upper()

  if len(kode) != 8:
    return 'Gagal: Kode harus berjumlah 8 karakter!!'

  if not kode.startswith(PROMO):
    return 'Gagal: Kode harus diawali dengan kata PROMO'

  karakter_terakhir = kode[-1]

  if karakter_terakhir.isdigit():
    if angka % 2 == 0:
      return "BERHASIL: Kode promo dapat digunakan!"
    else:
      return "GAGAL: Karakter terakhir harus berupa angka."

input_user = input("Masukkan Kode Promo: ")
hasil = cek_promo(input_user)
print(hasil)