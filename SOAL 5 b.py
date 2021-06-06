# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 16:21:30 2021

@author: Aldo Pratama - 20083000014
"""

"KATEGORI USIA"

#Input Usia
print("KATEGORI USIA")
Usia = int(input ("Masukkan Umur"))

#Read Usia
if Usia >=60:
    print ("status : Lansia")
elif Usia >=35:
    print ("status : Dewasa")
elif Usia >=18:
    print ("status : Pemuda")
elif Usia >=15:
    print ("status : Remaja")
else:
    print ("status : Anak")