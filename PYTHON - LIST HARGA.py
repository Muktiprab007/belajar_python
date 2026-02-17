daftar_harga = []

while True:
  nama = input('Masukkan nama barang: ')
  if nama == 'selesai':
    break
  harga = int(input('masukkan harga barang: '))

  daftar_harga.append(harga)
  
total = sum(daftar_harga)

diskon = 0

if total > 100000:
  diskon = 0.10
elif total > 200000:
  diskon = 0.20

total_potongan = total * diskon
total_harga = total - total_potongan

print("\n--- STRUK BELANJA ---")
print(f"Total Awal    : Rp{total}")
print(f"Diskon        : Rp{int(total_potongan)}")
print(f"Harus Dibayar : Rp{int(total_harga)}")
