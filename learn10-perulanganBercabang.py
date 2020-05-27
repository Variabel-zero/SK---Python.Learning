"""
	---Loop
	---- For In ==> untuk mengerurka isi list
"""

a = 1

while a < 5 :
	b = 0
	while b < a :
		print("*", end=' ')
		b += 1
	print()
	a +=1

#coba dengan for In
#range(1,5) artinya pasang angka dari 1 - 4
for i in range(1,5):
	for j in range(1,5):
		c = i*j
		print(c,end=' ')
	print()