# -*- coding: utf-8 -*-
"""
@author: Aldo Pratama - 20083000014
UTS Algoritma
Soal 2.
"""

JawabUlang = "y"
while JawabUlang=="y" or JawabUlang=="Y":
    print("==============================================")
    print("                BENGKEL MOTOR UD              ")
    print("              TRANSAKSI BIAYA OLI             ")
    print("==============================================")
    print("            DAFTAR MERK OLI MOTOR :")
    print("            a. Duration SW20 1L")
    print("            b. Castrol Magnatec 1L")
    print("            c. Federal Supreme XX 1L")
    print("            d. Yamalube 1L")
    print("            e. Shell 1L")
    print(" ")

#masukkan nilai variabel
    kode =['a','b','c','d','e']
    merkoli = ['Duration SW20 1L','Castrol Magnatec 1L','Federal Supreme XX 1L','Yamalube 1L','Shell 1L']
    harga = [53000,50000,54000,45000,46000]
    persenDiskon = 0.05
    ppn = 0.01
    minDiskon = 200000
    TotalAwal = 0
    NilaiDiskon = 0
    
#input kode oli
    pilihan = input(">> Masukkan Kode Oli = ")

#identifikasi indeks
    idx = 0
    while idx < len(kode):
        if kode[idx] == pilihan:

            print(">> Merk Oli = " + merkoli[idx])
            print(">> Harga Oli = Rp " + str (harga[idx]))
            
#tahap hitung biaya awal
    Qty = int(input(">> Masukkan Jumlah Oli yang dibeli = "))
    
    if Qty > 0:
        TotalAwal = harga[idx] * int(Qty)
        print(">> Total Awal= Rp " + str(TotalAwal))
            
        jmlppn = float(ppn) * harga[idx] * Qty
        print(">> PPN 1% = " + str (jmlppn))
            
#Cek Nilai Diskon
    if (TotalAwal) > minDiskon:
        NilaiDiskon = int(TotalAwal) * float(persenDiskon)
    print("Potongan Harga 5%")
    print(">> Jumlah Potongan Harga =     " + str(NilaiDiskon))
    
    else:
        print(">> Jumlah Potongan Harga = 0")
            
#Total Pembayaran
    TotalBayar = int(TotalAwal) - int(NilaiDiskon) + ppn
    print(">>> Total yang harus dibayarkan  = Rp " + str(TotalBayar))
    print("==========================================================================")
            
    idx = idx + 1

#inputan untuk break
    print(" ")
    print(" ^^ Note : Masukkan Kode Oli yang tertera ^^")
    JawabUlang = input(">>> Apakah Anda ingin melakukan transaksi lagi ? y/t : ")
    if JawabUlang== "t" or JawabUlang =="T":
      break