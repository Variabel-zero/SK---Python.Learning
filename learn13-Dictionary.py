"""
Sequances

Tuples =  List yang sifatnya immutable / datanya mutlak tidak bisa di ubah ( ditambah,deit,dihapus)
Tuple mengugnakan {}

"""

data = {'nama' : 'Satriawan',
		'umur' : '21',
		'hobby' : 'Membaca'
		}

print(data)

#tambah data

data['cita'] = 'Makan sepuasnya'
print(data)

#edit data
data['cita'] = 'Programmer full stack'
print(data)

#delite data 
del data['cita']
print(data)

#menggunkan perulanagn deng dictionary
for key,value in data.items():
	print(key,"sama dengan "+value)