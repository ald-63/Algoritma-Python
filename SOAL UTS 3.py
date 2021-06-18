# -*- coding: utf-8 -*-
"""
@author: Aldo Pratama - 20083000014
UTS Algoritma
Soal 2.
"""

#import waktu (tanggal dan jam)
import datetime

datetime_object = datetime.datetime.now()
print(datetime_object)
print(" ")

JawabUlang = "y"
while JawabUlang=="y" or JawabUlang=="Y":
    print("=======================================================")
    print("                     TOKO UD SUBUR              ")
    print("            TRANSAKSI BIAYA BAHAN BANGUNAN             ")
    print("=======================================================")
    print("               DAFTAR BAHAN BANGUNAN :")
    print("               a. Asbes Gelombang")
    print("               b. Cat Tembok Dulux 1Galon")
    print("               c. Cat Tembok Dulux 1Galon")
    print("               d. Aquaproof 5 Kg")
    print("               e. Seng 2mm")
    print("               f. Spandeks 1mm")
    print(" ")
#masukkan nilai variabel
    kode =['a','b','c','d','e','f']
    barang = ['Asbes Gelombang','Cat Tembok Dulux 1Galon','Cat Tembok Dulux 1Galon','Aquaproof 5 Kg','Seng 2mm','Spandeks 1mm']
    harga = [60000,250000,350000,50000,70000,92000]
    persenDiskon = 0.05
    ppn = 0.02
    minDiskon = 500000
    TotalAwal = 0
    NilaiDiskon = 0
    
#input kode oli
    pilihan = input(">> Masukkan Kode Barang                = ")

#identifikasi indeks
    idx = 0
    while idx < len(kode):
        if kode[idx] == pilihan:
            print(">> Barang                              = " + barang[idx])
            print(">> Harga Barang                        = Rp " + str(harga[idx]))
            break
    
#tahap hitung biaya awal
    Qty = int(input(">> Masukkan Jumlah Barang yang dibeli  = "))
    if Qty > 0:
        TotalAwal = harga[idx] * int(Qty)
        print(">> Total Awal                          = Rp " + str(TotalAwal))
            
        jmlppn = float(ppn) * harga[idx] * Qty
        print(">> PPN 2%                              = " + str (jmlppn))
            
#Cek Nilai Diskon
    if (TotalAwal) > minDiskon:
        NilaiDiskon = int(TotalAwal) * float(persenDiskon)
        print("                                       Anda Mendapat Potongan Harga 5%")
        print(">> Jumlah Potongan Harga               = " + str(NilaiDiskon)) 
            
#Total Pembayaran
    TotalBayar = int(TotalAwal) - int(NilaiDiskon) + ppn
    print(">>> Total yang harus dibayarkan        = Rp " + str(TotalBayar))
    print("=======================================================")
            
    idx = idx + 1

#inputan untuk break
    print(" ")
    print(" ^^ Note : Masukkan Kode Barang yang tertera ^^")
    JawabUlang = input(">>> Apakah Anda ingin melakukan transaksi lagi ? y/t : ")
    if JawabUlang== "t" or JawabUlang =="T":
      break