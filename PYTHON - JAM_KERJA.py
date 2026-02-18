nama = input("Nama Karyawan: ")
jam_kerja = int(input("Total Jam Kerja Sebulan: "))
rating = input("Rating Performa (A/B/C): ").upper()

gaji_pokok = 5000000
total_lembur = 0
bonus = 0

if jam_kerja > 160:
    jam_lembur = jam_kerja - 160
    total_lembur = jam_lembur * 50000

if rating == 'A':
    bonus = 1000000
elif rating == 'B':
    bonus = 500000

total_kotor = gaji_pokok + total_lembur + bonus

pajak = 0
if total_kotor > 7000000:
    pajak = total_kotor * 0.05

total_bersih = total_kotor - pajak

print(f"Gaji Pokok: Rp{gaji_pokok}")
print(f"Lembur    : Rp{total_lembur}")
print(f"Bonus     : Rp{bonus}")
print(f"Pajak     : Rp{int(pajak)}")
print(f"TOTAL DITERIMA: Rp{int(total_bersih)}")