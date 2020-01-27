#!/usr/bin/python
# coding: utf8
import cgi
import string

form = cgi.FieldStorage()
sequence_dna = form.getfirst("sequence_dna", "0") #Забрал данные, введенные в форму в редакторе html из панели управления

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <link rel="stylesheet" type="text/css" href="GC_content.css">
            <title>Обработка данных форм</title>
        </head>
        <body>""")
print("<h2>Результаты:</h2>")

G_content = int(0)
C_content = int(0)
A_content = int(0)
T_content = int(0)
percent_G = float(0)
percent_C = float(0)
percent_A = float(0)
percent_T = float(0)

n = len(sequence_dna)
sequence_dna = sequence_dna.upper()
for i in range(0, n):
    if sequence_dna[i] == "G" : G_content += 1
    if sequence_dna[i] == "C" : C_content += 1
    if sequence_dna[i] == "A" : A_content += 1
    if sequence_dna[i] == "T" : T_content += 1
common_base = G_content + C_content + A_content + T_content
percent_G = G_content/float(common_base)*100
percent_C = C_content/float(common_base)*100
percent_A = A_content/float(common_base)*100
percent_T = T_content/float(common_base)*100
print('<p>GC состав = <b>%.1f %%</b></p>' % (percent_G + percent_C))
print('<p>Содержание G = <b>%.1f %%</b></p>' % (percent_G))
print('<p>Содержание C = <b>%.1f %%</b></p>' % (percent_C))
print('<p>Содержание A = <b>%.1f %%</b></p>' % (percent_A))
print('<p>Содержание T = <b>%.1f %%</b></p>' % (percent_T))
print('<p>Общая длина = <b>%i</b> нуклеотида/ов</p>' % (common_base))

print("<p><b>Исходная последовательность ДНК:</b></p>")
for i in range(0, len(sequence_dna), 50):
    print "<p><h3>", sequence_dna[i:i+10], " ", sequence_dna[i+10:i+20], " ", sequence_dna[i+20:i+30], " ", sequence_dna[i+30:i+40], " ", sequence_dna[i+40:i+50], "</h3></p>"

print("""</body>
        </html>""")