if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    # 1. Ubah map menjadi list agar bisa diolah
    list_angka = list(arr)
    
    # 2. Hapus angka duplikat dengan set()
    # Misal: [2, 3, 6, 6, 5] menjadi {2, 3, 5, 6}
    angka_unik = set(list_angka)
    
    # 3. Urutkan dari terkecil ke terbesar
    angka_urut = sorted(list(angka_unik))
    
    # 4. Ambil angka kedua dari belakang (indeks -2)
    # Ini adalah nilai terbesar kedua (Runner-Up)
    print(angka_urut[-2])