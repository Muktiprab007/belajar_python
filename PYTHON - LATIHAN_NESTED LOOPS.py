perpustakaan = [
    [1, 0, 1], # Rak 0 (Fiksi)
    [0, 1, 0], # Rak 1 (Sains)
    [1, 0, 0]  # Rak 2 (Sejarah)
]

kategori = {0: "Fiksi", 1: "Sains", 2: "Sejarah"}
total_kosong = 0
for i in range(len(perpustakaan)):
  nama_rak = kategori[i]

  for buku in perpustakaan[i]:
    if buku == 0:
      print(f"Ada ruang kosong di Rak {nama_rak}")
      total_kosong += 1

print(f"\nTotal Ruang Kosong: {total_kosong}")