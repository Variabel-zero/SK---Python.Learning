
player1 = {'name':'Sunggoku','power':100}
player2 = {'name':'Luffy','power':200}

def latihan(palyer):
	palyer['power'] += 100

def tarung(penyerang,penahan):
	if penyerang['power'] < penahan['power']:
		print("Anda masih kurang kuat ",penyerang['name'])
	elif penyerang['power'] > penahan['power']:
		print("Anda Menang ",penyerang['name'])
	else:
		print("Seri")

latihan(player1)
tarung(player1,player2)