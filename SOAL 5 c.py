# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 16:34:43 2021

@author: Aldo Pratama - 20083000014
"""

"STATUS NILAI"

#Input Status Nilai
print ("STATUS NILAI")
Nilai = int(input("Masukkan Nilai : "))

#Read Nilai
if Nilai >=80:
    print ("BAIK SEKALI")
elif Nilai >=65:
    print ("BAIK")
elif Nilai >=55:
    print ("CUKUP")
elif Nilai >=40:
    print ("KURANG")
elif Nilai <=39:
    print ("KURANG SEKALI")