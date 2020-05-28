"""
	Nested Distionaru sama dengan distionari biasa tapi, dalam entuk bercabang dan multi
"""

data = {
		1:{'nama' : 'Satriawan','umur' : '21','hoby' : "makan"},
		2:{'nama' : 'Abdul','umur' : '24','hoby' : "makan lagi"}
		}

print(data)


#menambpilkan dalam perulangan
for key, nilai in data.items():
	print("keynya-",key)
	#ambil nilai dari value esimpan ke key2
	for key2 in nilai:
		#print key2 yang berasal dari value dan print value dari key2 yang di ambil dari value sebelumya
		print(key2,"-",nilai[key2])