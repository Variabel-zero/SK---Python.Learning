#boolean
#nilainya hanya true atau false
x = 10
y = 25
#cek 
print(x < y) #nilai true
print(x > y) #nilai true

#cek numerik atau string
print("=====================")
nama = "Satriawan"
print(nama.isdigit()) #nilai false - isdigit() =(apakah value adalah numerik?)
print(nama.isalnum()) #nilai true - isalnum() = (apakah value adalah alfa numerik?)