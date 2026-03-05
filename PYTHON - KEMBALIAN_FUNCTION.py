def hitung_kembalian(total, bayar):
    kembalian = bayar - total
    
    if kembalian < 0:
        return 'Uang Tidak Cukup'
    if kembalian == 0:
        return 'Uang Pas, tidak ada kembalian'
    
    lembar_5rb = kembalian // 5000
    sisa = kembalian % 5000
    
    lembar_2rb = sisa // 2000
    sisa = sisa % 2000
    
    lembar_1rb = sisa // 1000
    
    hasil = f"Total Kembalian: Rp{kembalian}\n"
    hasil += f"- 5rb: {lembar_5rb} lembar\n"
    hasil += f"- 2rb: {lembar_2rb} lembar\n"
    hasil += f"- 1rb: {lembar_1rb} lembar"
    
    return hasil

print(hitung_kembalian(13000, 20000))

print(hitung_kembalian(21000, 50000))