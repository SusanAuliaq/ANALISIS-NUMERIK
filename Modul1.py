#algoritma1
#step 1: input nilai awal adalah angka yang besar
x_awal1 = 1000.0
#step 2: input nilai selanjutnya adalah angka yang kecil
x_selanjutnya1 = 0.0001
#step 3: melakukan perulangan
for _ in range(5):
  x_awal1 += x_selanjutnya1
#cetak hasil
print("Hasil penjumlahan algoritma 1 adalah:", x_awal1)

#Algoritma 2
Total2 =0.0
#input nilai awal  adalah angka yang kecil
x_awal2 = 0.0001
#melakukan perulangan sebanyak 5 kali
for _ in range (5):
  Total2 += x_awal2
Total2 += 1000.0
#cetak hasil
print("Hasil penjumlahan algoritma 2 adalah:", x_awal2)
