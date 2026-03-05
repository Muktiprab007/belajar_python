def enkripsi_rahasia(pesan):
    hasil_transformasi = ''
    vokal = 'AIUEOaiueo'
    
    for karakter in pesan:
        if karakter.isalpha():
            if karakter in vokal:
                huruf_baru = chr(ord(karakter) + 1)
                hasil_transformasi += huruf_baru.upper()
            else:
                hasil_transformasi += karakter.lower()
        else:
            continue
        
    pesan_final = hasil_transformasi[::-1]
    
    return pesan_final

pesan = input('Masukkan Pesan: ')
pesan_akhir = enkripsi_rahasia(pesan)
print(pesan_akhir)

print(f"Hasil Enkripsi: {enkripsi_rahasia('Python Mantap!')}")