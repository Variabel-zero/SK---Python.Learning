"""
	local dan global variabel 
	local bariabel ridak bisa diknali oleh variabel dari luar kecuali mengguanakn ey global
	sedangkan global bis adigunkan dimana saja
"""

nama2 = "Satriawan - Satriawan 0o123455"

def akses():
	global nama2 
	nama2 = "chucky"
	print("nama "+nama2)
	
print(nama2)
akses()