"""
	Function
	--- *Args (dari kata argumen)
	--- **Kwargs (keyword argumen)
"""

#contoh menggunkan *
def fuungsinya(*bebas):
	#jika ingn print satu  - satu
	for key in bebas: 
		print(key)


print(fuungsinya('Striawan','membaca'))


#contoh menggunakna **
def fuungsinya2(**bebas):
	#jika ingn print satu  - satu
	for key,nilai in bebas.items(): 
		print(key + " - "+nilai)


print(fuungsinya2(nama = 'Satriawan',hobi='membaca',cita='programer'))