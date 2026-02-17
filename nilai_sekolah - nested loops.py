data_sekolah = [
    [["Andi", 85], ["Budi", 90], ["Cici", 80]],  # Kelas A (Index 0)
    [["Dodi", 70], ["Eka", 95], ["Fani", 88]],   # Kelas B (Index 1)
    [["Gita", 92], ["Hadi", 85], ["Iwan", 75]]    # Kelas C (Index 2)
]

for i in range(len(data_sekolah)):
  kelas = data_sekolah[i]
  total = 0
  siswa_terbaik = ''
  tertinggi = 0

  for siswa in kelas:
    nama = siswa[0]
    nilai = siswa[1]

    total += nilai

    if nilai > tertinggi:
      tertinggi = nilai
      siswa_terbaik = nama

  rata_rata = total / len(kelas)

  print(rata_rata)
  print(siswa_terbaik)
  print(tertinggi)