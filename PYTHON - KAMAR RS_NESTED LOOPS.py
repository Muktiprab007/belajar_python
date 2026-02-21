# List 2D: Baris = Lantai, Kolom = Jenis Kamar
monitor_rs = [
    [1, 0, 1], # Lantai 1
    [0, 1, 0], # Lantai 2
    [1, 1, 0]  # Lantai 3
]

# Kamus Nama Baris (Lantai)
label_lantai = {0: "Lantai Dasar", 1: "Lantai 1", 2: "Lantai VIP"}

# Kamus Nama Kolom (Jenis Kamar)
label_kamar = {0: "Kamar Reguler", 1: "Kamar Anak", 2: "Kamar Isolasi"}

total_kosong = 0

for lantai in range(len(monitor_rs)):
  nama_lantai = label_lantai[lantai]
  for kamar in range(len(monitor_rs[i])):
    nama_kamar = label_kamar[kamar]
    status = monitor_rs[lantai][kamar]

    if status == 0:
      print(f'INFO: {nama_kamar} di {nama_lantai} sedang KOSONG.')
      total_kosong += 1
print(f"\nTotal Bed Tersedia: {total_kosong}")