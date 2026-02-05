def is_leap(n):
  leap = False

  if n % 4 == 0:
    if n % 100 == 0:
      if n % 400 == 0:
        leap = True
      else:
        leap = False
    else:
      leap = True
  else:
    leap = False

  return leap

n = int (input('Masukkan Input: '))
print(f'ini adalah: {is_leap(n)}')