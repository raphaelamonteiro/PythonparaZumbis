a = int(input("ano: "))
if a % 4 == 0 and (a % 100 != 0 or a % 400 == 0):
  print ("é bissexto")
else:
  print ("não é bissexto")
