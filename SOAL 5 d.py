# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 17:28:35 2021

@author:  Aldo Pratama - 20083000014
"""

"KATEGORI NILAI"

#Input Kategori Nilai
print("KATEGORI NILAI")
Nilai = int(input ("Masukkan Nilai : "))

#Read Nilai
if Nilai >=91 and Nilai <=100:
    print ("A")
elif Nilai >=81 and Nilai <=91:
    print ("B")
elif Nilai >=71 and Nilai <=81:
    print ("C")
elif Nilai <=71:
    print ("D")