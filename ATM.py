pin = '1234'
kesempatan = 3

while kesempatan > 0:
  input_pin = input('Masukkan PIN: ')

  if input_pin == pin:
    print('Selamat Datang')
    break
  else:
    kesempatan -= 1
    if kesempatan > 0:
      print ('coba lagi')
    else:
      print ('akun anda diblokir')