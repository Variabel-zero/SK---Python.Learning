
#buat program bayar utang sedeerhana
uang = input("Kamu punya uang berapa? ")
hutang = 10000

if int(uang) < hutang :
	print("Terima kasih,")
	print("uangnya kurang ",hutang-int(uang))
elif int(uang) == hutang :
	print("uangnya pas")
else :
	print("Terima kasih,")
	print("uangnya lebih ",int(uang)-hutang)

