# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 17:36:22 2021

@author: Aldo Pratama - 20083000014
"""

"TRANSAKSI PEMBELIAN PRINTER EPSON"

#Nilai awal variabel JmlBeli = Harga 1 Printer
HargaPrint = 660000

#Input Jumlah Beli
print("TRANSAKSI PEMBELIAN PRINTER EPSON T20")
JmlBeli = input("Jumlah Printer Epson T20 Yang Dibeli = ")

#Proses Hitung Total
Total = int(HargaPrint)*int(JmlBeli)

#Tampil
print("Total Transaksi Pembelian Printer Epson T20 = Rp " + str(Total))