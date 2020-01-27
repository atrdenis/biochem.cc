#!/usr/bin/python
# coding: utf8
import cgi
import string
from math import log10, floor

form = cgi.FieldStorage()
molarity = form.getfirst("molarity", "0") # в моль/л
volume = form.getfirst("volume", "0") # в литрах
MW = form.getfirst("MW", "0") # в г/моль

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
MW = float(MW.replace(',','.'))

n_amount = 6 #число значащих цифр

amount_mol = molarity * volume #всего моль
mass_g = amount_mol * MW #масса в граммах
mass_mg = mass_g * 1000 #масса в милиграммах

mass_g = round(mass_g, -int(floor(log10(abs(mass_g))))+n_amount-1) #округляем до необходимого числа значащих цифр
mass_mg = round(mass_mg, -int(floor(log10(abs(mass_mg))))+n_amount-1)
mass_g = int(mass_g) if not mass_g%1 else mass_g #убираем нули, если они остались после запятой
mass_mg = int(mass_mg) if not mass_mg%1 else mass_mg


print "<p>Масса навески (в г) = <b>", mass_g, "</b></p>"
print "<p>Масса навески (в мг) = <b>", mass_mg, "</b></p>"

print("""</body>
        </html>""")