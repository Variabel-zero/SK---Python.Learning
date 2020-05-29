"""
	latihan membuat game tamagochi
"""

nama = input("Apa nama mosternya?")
moster = {'name' : nama,'power' : 100}

def starGame():
	pilihan = input("mau apa? 1.makan 2.lihatStatus 3.keluar : ")
	if pilihan == "1":
		makan()
	elif pilihan == "2":
		status()
	else :
		print("bye.. byee")


def makan():
	print("nyam...nyamm")
	moster['power'] += 100
	starGame()

def status():
	print("staus  :",moster['power'])
	starGame()


starGame()