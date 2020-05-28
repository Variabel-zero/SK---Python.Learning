"""
 Set sama dengan distionery menggunakan tanda{} tapi nilainya tidak memiliki index, tidak punya urutan dan tidak bisa di duplikat
 """

orang = {'Satriawan','Agus','Anang'} 
print(orang)

#tamabah data dengan
orang.add('Hasan')
print(orang)

#hapus data dengan
orang.remove('Agus')
print(orang)


#yang menarik kita bisa menggunakan operasi arimtika "LOGIKA INFORMATIKA"
angka1 = {1,2,3,4,5}
angka2 = {4,5,6,7,8}

#operator atau | akan menghasilkan semua data tapi tidak ada yang sama
print(angka1 | angka2) #union

#operator and & akan menampilkan data yang sama saja
print(angka1 & angka2) #irisan atau intersection

#operator minus hanya menampilkan data yang berbeda dari data yang lain (akan menampilkan apa yang berbeda rai anka datu di angka 2)
print(angka1 - angka2) #differens (tergantung posisi parameter)

#operator ^ bukan perbedaan akan menampilkan data yang tidak ada kembarnya
print(angka1 | angka2) #tidak sama