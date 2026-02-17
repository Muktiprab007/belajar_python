n = int(input('Masukkan Bilangan Prima: '))

if n <= 1:
    print ('Angka yang anda masukkan bukan bilangan prima')
else:
    is_prima = True
    
    for i in range (2, n):
        if n % i == 0:
            is_prima = False
            break
    
    if is_prima:
        print(f'{n} adalah bilangan Prima')
    else:
        print(f'{n} Bukan bilangan prima')
