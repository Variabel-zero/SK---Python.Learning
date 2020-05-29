#ambil data dari file forlearn20.py


# #cara 1 impor data
# import forlearn20 
# print(forlearn20.orang)
# forlearn20.masuknama('Satriawan')

# #cara 2 ganti nama import
# import forlearn20 as data
# print(data.orang)
# forlearn20.masuknama('Satriawan')


# #cara 3 impor data lebih spesifik
# from forlearn20 import orang
# print(orang)

#yang aktifcuman yang dipanggill jika spesifik
from forlearn20 import masuknama
print(masuknama('Satriawan'))

