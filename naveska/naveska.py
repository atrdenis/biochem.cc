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


molarity = float(molarity)
volume = float(volume)
MW = float(MW)
n_amount = 6 #число значащих цифр

amount_mol = molarity * volume #всего моль
mass_g = amount_mol * MW #масса в граммах
mass_mg = mass_g * 1000 #масса в милиграммах

mass_g = round(mass_g, -int(floor(log10(abs(mass_g))))+n_amount-1)
mass_mg = round(mass_mg, -int(floor(log10(abs(mass_mg))))+n_amount-1)
print(mass_g, mass_mg)


'''print('<p>GC состав = <b>%.1f %%</b></p>' % (percent_G + percent_C))
print('<p>Содержание G = <b>%.1f %%</b></p>' % (percent_G))
print('<p>Содержание C = <b>%.1f %%</b></p>' % (percent_C))
print('<p>Содержание A = <b>%.1f %%</b></p>' % (percent_A))
print('<p>Содержание T = <b>%.1f %%</b></p>' % (percent_T))
print('<p>Общая длина = <b>%i</b> нуклеотида/ов</p>' % (common_base))
'''

print("""</body>
        </html>""")
'''