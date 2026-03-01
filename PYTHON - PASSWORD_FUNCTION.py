def cek_keamanan_password(password):
    skor = 0
    
    if len(password) >= 8:
        skor += 1
    
    ada_angka = False
    for karakter in password:
        if karakter.isdigit():
            ada_angka = True
            break
    if ada_angka:
        skor += 1
            
    ada_huruf_besar = False
    for karakter in password:
        if karakter.isupper():
            ada_huruf_besar = True
            break
    if ada_huruf_besar:
        skor += 1

    if skor == 3:
        return "Kuat"
    elif skor == 2:
        return "Sedang"
    else:
        return "Lemah"

pw_user = input("Masukkan password baru: ")
hasil = cek_keamanan_password(pw_user)

print(f"Kekuatan password kamu: {hasil}")