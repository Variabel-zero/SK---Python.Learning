"""
Sequances

Tuples =  List yang sifatnya immutable / datanya mutlak tidak bisa di ubah ( ditambah,deit,dihapus)
Tuple mengugnakan ()

"""

orang = ('Satria','Hasan','abdul')
orang1 = ['Satria','Hasan','abdul']

print(orang)

#tuples bisa menggunakn metode biasa seperti len,max,min
#menghitung panjang data
print(len(orang[2]))

#mengubah tuples menjadi list
print(list(orang))

#mengubah list menjadi tupples
print(tuple(orang1))