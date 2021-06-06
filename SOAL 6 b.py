# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 18:09:48 2021

@author: Aldo Pratama - 20083000014
"""

"TRANSAKSI PEMBELIAN PRINTER EPSON T20 (DISKON)"

#Nilai Awal
minDiskon = 1500000
persenDiskon = 0.15
HrgSat = 660000
TotalAwal = 0
NilaiDiskon = 0

#Hitung total awal
print("TRANSAKSI PEMBELIAN PRINTER EPSON T20 (DISKON)")
Qty = int(input("Masukkan Jumlah Printer yang dibeli = "))
if Qty > 0:
    TotalAwal = int(HrgSat) * int(Qty)
    print("Total Awal = Rp " + str(TotalAwal))
else:
    print("Cek kembali jumlah Printer yang dibeli")
    
#Cek Nilai Diskon
if (TotalAwal) > minDiskon:
    NilaiDiskon = int(TotalAwal) * float(persenDiskon)
    print("Nilai Diskon = " + str(NilaiDiskon))
else:0

#Total Bayar
TotalBayar = int(TotalAwal) - int(NilaiDiskon)
print("Total yang harus dibayarkan = Rp " + str(TotalBayar))