#!/usr/bin/python
# coding: utf8
#from BIOCHEM.CC
import cgi
import string
import numpy as np
from math import log10, floor


form = cgi.FieldStorage()
molarity = form.getfirst("molarity", "0") # в моль/л
volume = form.getfirst("volume", "0") # в литрах
pH = form.getfirst("pH", "0") # в г/моль

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <link rel="stylesheet" type="text/css" href="naveska.css">
            <title>Обработка данных форм</title>
        </head>
        <body>""")
print("<h2>Результаты:</h2>")

molarity = float(molarity.replace(',','.'))
volume = float(volume.replace(',','.'))
pH = float(pH.replace(',','.'))


pH_Tris_25 = np.array([[7.2, 0.67, 7.02],
[7.3, 0.8, 6.85],
[7.4, 0.97, 6.61],
[7.5, 1.18, 6.35],
[7.6, 1.39, 6.06],
[7.7, 1.66, 5.72],
[7.8, 1.97, 5.32],
[7.9, 2.3, 4.88],
[8, 2.65, 4.44],
[8.1, 2.97, 4.02],
[8.2, 3.34, 3.54],
[8.3, 3.7, 3.07],
[8.4, 4.03, 2.64],
[8.5, 4.36, 2.21],
[8.6, 4.65, 1.83],
[8.7, 4.9, 1.5],
[8.8, 5.13, 1.23],
[8.9, 5.32, 0.96],
[9, 5.47, 0.76]])

pH_above_indexes = np.where(pH_Tris_25[:,0] >= pH)
pH_above = pH_Tris_25[pH_above_indexes[0][0],0]
pH_below = pH_Tris_25[pH_above_indexes[0][0]-1,0]
TrisBase_mass = (pH_above-pH)/(pH_above-pH_below)*pH_Tris_25[pH_above_indexes[0][0]-1,1]+\
(pH-pH_below)/(pH_above-pH_below)*pH_Tris_25[pH_above_indexes[0][0],1]
TrisHCl_mass = (pH_above-pH)/(pH_above-pH_below)*pH_Tris_25[pH_above_indexes[0][0]-1,2]+\
(pH-pH_below)/(pH_above-pH_below)*pH_Tris_25[pH_above_indexes[0][0],2]
TrisBase_mass_end = TrisBase_mass/0.05*molarity*volume
TrisHCl_mass_end = TrisHCl_mass/0.05*molarity*volume

n_amount = 5 #число значащих цифр

TB_g = round(TrisBase_mass_end, -int(floor(log10(abs(TrisBase_mass_end))))+n_amount-1) #округляем до необходимого числа значащих цифр
TB_g = int(TB_g) if not TB_g%1 else TB_g #убираем нули, если они остались после запятой

TCl_g = round(TrisHCl_mass_end, -int(floor(log10(abs(TrisHCl_mass_end))))+n_amount-1) #округляем до необходимого числа значащих цифр
TCl_g = int(TCl_g) if not TCl_g%1 else TCl_g #убираем нули, если они остались после запятой

if pH <7.2 or pH > 9 :
	print("pH вне диапазона 7,2 - 9,0")
else:
	print "<p>Масса TrisBase = <b>", TB_g, "</b> г </p>"
	print "<p>Масса TrisHCl = <b>", TCl_g, "</b> мг </p>"

print("""</body>
        </html>""")

