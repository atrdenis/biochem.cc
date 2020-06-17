#!/usr/bin/python
# coding: utf8
import cgi
import string
import re

form = cgi.FieldStorage()
sequence_dna = form.getfirst("sequence_dna", "0") #Забрал данные, введенные в форму в редакторе html из панели управления
sequence_dna = sequence_dna.replace("\r","")
sequence_dna = sequence_dna.replace("\n","")
sequence_dna = sequence_dna.upper()
sequence_dna = re.sub("[^ACTG]+", "", sequence_dna)

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <link rel="stylesheet" type="text/css" href="dna_to_prot.css">
            <title>Обработка данных форм</title>
        </head>
        <body>""")
print("<h2>Результаты:</h2>")

sequence_prot_1 = ""
sequence_prot_2 = ""
sequence_prot_3 = ""

n = len(sequence_dna)
for i in range(0, n, 3):
    if sequence_dna[i:i+3] == "GCT" or sequence_dna[i:i+3] ==  "GCC" or sequence_dna[i:i+3] ==  "GCA" or sequence_dna[i:i+3] ==  "GCG": sequence_prot_1 += "A"
    if sequence_dna[i:i+3] == "TTA" or sequence_dna[i:i+3] ==  "TTG" or sequence_dna[i:i+3] ==  "CTT" or sequence_dna[i:i+3] ==  "CTC" or sequence_dna[i:i+3] ==  "CTA" or sequence_dna[i:i+3] ==  "CTG": sequence_prot_1 += "L"
    if sequence_dna[i:i+3] == "CGT" or sequence_dna[i:i+3] ==  "CGC" or sequence_dna[i:i+3] ==  "CGA" or sequence_dna[i:i+3] ==  "CGG" or sequence_dna[i:i+3] ==  "AGA" or sequence_dna[i:i+3] ==  "AGG": sequence_prot_1 += "R"
    if sequence_dna[i:i+3] == "AAA" or sequence_dna[i:i+3] ==  "AAG": sequence_prot_1 += "K"
    if sequence_dna[i:i+3] == "AAT" or sequence_dna[i:i+3] ==  "AAC": sequence_prot_1 += "N"
    if sequence_dna[i:i+3] == "ATG": sequence_prot_1 += "M"
    if sequence_dna[i:i+3] == "GAT" or sequence_dna[i:i+3] ==  "GAC": sequence_prot_1 += "D"
    if sequence_dna[i:i+3] == "TTT" or sequence_dna[i:i+3] ==  "TTC": sequence_prot_1 += "F"
    if sequence_dna[i:i+3] == "TGT" or sequence_dna[i:i+3] ==  "TGC": sequence_prot_1 += "C"
    if sequence_dna[i:i+3] == "CCT" or sequence_dna[i:i+3] ==  "CCC" or sequence_dna[i:i+3] ==  "CCA" or sequence_dna[i:i+3] ==  "CCG": sequence_prot_1 += "P"
    if sequence_dna[i:i+3] == "CAA" or sequence_dna[i:i+3] ==  "CAG": sequence_prot_1 += "Q"
    if sequence_dna[i:i+3] == "TCT" or sequence_dna[i:i+3] ==  "TCC" or sequence_dna[i:i+3] ==  "TCA" or sequence_dna[i:i+3] ==  "TCG" or sequence_dna[i:i+3] ==  "AGT" or sequence_dna[i:i+3] ==  "AGC": sequence_prot_1 += "S"
    if sequence_dna[i:i+3] == "GAA" or sequence_dna[i:i+3] ==  "GAG": sequence_prot_1 += "E"
    if sequence_dna[i:i+3] == "ACT" or sequence_dna[i:i+3] ==  "ACC" or sequence_dna[i:i+3] ==  "ACA" or sequence_dna[i:i+3] ==  "ACG": sequence_prot_1 += "T"
    if sequence_dna[i:i+3] == "GGT" or sequence_dna[i:i+3] ==  "GGC" or sequence_dna[i:i+3] ==  "GGA" or sequence_dna[i:i+3] ==  "GGG": sequence_prot_1 += "G"
    if sequence_dna[i:i+3] == "TGG": sequence_prot_1 += "W"
    if sequence_dna[i:i+3] == "CAT" or sequence_dna[i:i+3] ==  "CAC": sequence_prot_1 += "H"
    if sequence_dna[i:i+3] == "TAT" or sequence_dna[i:i+3] ==  "TAC": sequence_prot_1 += "Y"
    if sequence_dna[i:i+3] == "ATT" or sequence_dna[i:i+3] ==  "ATC" or sequence_dna[i:i+3] ==  "ATA": sequence_prot_1 += "I"
    if sequence_dna[i:i+3] == "GTT" or sequence_dna[i:i+3] ==  "GTC" or sequence_dna[i:i+3] ==  "GTA" or sequence_dna[i:i+3] ==  "GTG": sequence_prot_1 += "V"
    if sequence_dna[i:i+3] == "TAA" or sequence_dna[i:i+3] ==  "TGA" or sequence_dna[i:i+3] ==  "TAG": sequence_prot_1 += "*"
for i in range(1, n, 3):
    if sequence_dna[i:i+3] == "GCT" or sequence_dna[i:i+3] ==  "GCC" or sequence_dna[i:i+3] ==  "GCA" or sequence_dna[i:i+3] ==  "GCG": sequence_prot_2 += "A"
    if sequence_dna[i:i+3] == "TTA" or sequence_dna[i:i+3] ==  "TTG" or sequence_dna[i:i+3] ==  "CTT" or sequence_dna[i:i+3] ==  "CTC" or sequence_dna[i:i+3] ==  "CTA" or sequence_dna[i:i+3] ==  "CTG": sequence_prot_2 += "L"
    if sequence_dna[i:i+3] == "CGT" or sequence_dna[i:i+3] ==  "CGC" or sequence_dna[i:i+3] ==  "CGA" or sequence_dna[i:i+3] ==  "CGG" or sequence_dna[i:i+3] ==  "AGA" or sequence_dna[i:i+3] ==  "AGG": sequence_prot_2 += "R"
    if sequence_dna[i:i+3] == "AAA" or sequence_dna[i:i+3] ==  "AAG": sequence_prot_2 += "K"
    if sequence_dna[i:i+3] == "AAT" or sequence_dna[i:i+3] ==  "AAC": sequence_prot_2 += "N"
    if sequence_dna[i:i+3] == "ATG": sequence_prot_2 += "M"
    if sequence_dna[i:i+3] == "GAT" or sequence_dna[i:i+3] ==  "GAC": sequence_prot_2 += "D"
    if sequence_dna[i:i+3] == "TTT" or sequence_dna[i:i+3] ==  "TTC": sequence_prot_2 += "F"
    if sequence_dna[i:i+3] == "TGT" or sequence_dna[i:i+3] ==  "TGC": sequence_prot_2 += "C"
    if sequence_dna[i:i+3] == "CCT" or sequence_dna[i:i+3] ==  "CCC" or sequence_dna[i:i+3] ==  "CCA" or sequence_dna[i:i+3] ==  "CCG": sequence_prot_2 += "P"
    if sequence_dna[i:i+3] == "CAA" or sequence_dna[i:i+3] ==  "CAG": sequence_prot_2 += "Q"
    if sequence_dna[i:i+3] == "TCT" or sequence_dna[i:i+3] ==  "TCC" or sequence_dna[i:i+3] ==  "TCA" or sequence_dna[i:i+3] ==  "TCG" or sequence_dna[i:i+3] ==  "AGT" or sequence_dna[i:i+3] ==  "AGC": sequence_prot_2 += "S"
    if sequence_dna[i:i+3] == "GAA" or sequence_dna[i:i+3] ==  "GAG": sequence_prot_2 += "E"
    if sequence_dna[i:i+3] == "ACT" or sequence_dna[i:i+3] ==  "ACC" or sequence_dna[i:i+3] ==  "ACA" or sequence_dna[i:i+3] ==  "ACG": sequence_prot_2 += "T"
    if sequence_dna[i:i+3] == "GGT" or sequence_dna[i:i+3] ==  "GGC" or sequence_dna[i:i+3] ==  "GGA" or sequence_dna[i:i+3] ==  "GGG": sequence_prot_2 += "G"
    if sequence_dna[i:i+3] == "TGG": sequence_prot_2 += "W"
    if sequence_dna[i:i+3] == "CAT" or sequence_dna[i:i+3] ==  "CAC": sequence_prot_2 += "H"
    if sequence_dna[i:i+3] == "TAT" or sequence_dna[i:i+3] ==  "TAC": sequence_prot_2 += "Y"
    if sequence_dna[i:i+3] == "ATT" or sequence_dna[i:i+3] ==  "ATC" or sequence_dna[i:i+3] ==  "ATA": sequence_prot_2 += "I"
    if sequence_dna[i:i+3] == "GTT" or sequence_dna[i:i+3] ==  "GTC" or sequence_dna[i:i+3] ==  "GTA" or sequence_dna[i:i+3] ==  "GTG": sequence_prot_2 += "V"
    if sequence_dna[i:i+3] == "TAA" or sequence_dna[i:i+3] ==  "TGA" or sequence_dna[i:i+3] ==  "TAG": sequence_prot_2 += "*"
for i in range(2, n, 3):
    if sequence_dna[i:i+3] == "GCT" or sequence_dna[i:i+3] ==  "GCC" or sequence_dna[i:i+3] ==  "GCA" or sequence_dna[i:i+3] ==  "GCG": sequence_prot_3 += "A"
    if sequence_dna[i:i+3] == "TTA" or sequence_dna[i:i+3] ==  "TTG" or sequence_dna[i:i+3] ==  "CTT" or sequence_dna[i:i+3] ==  "CTC" or sequence_dna[i:i+3] ==  "CTA" or sequence_dna[i:i+3] ==  "CTG": sequence_prot_3 += "L"
    if sequence_dna[i:i+3] == "CGT" or sequence_dna[i:i+3] ==  "CGC" or sequence_dna[i:i+3] ==  "CGA" or sequence_dna[i:i+3] ==  "CGG" or sequence_dna[i:i+3] ==  "AGA" or sequence_dna[i:i+3] ==  "AGG": sequence_prot_3 += "R"
    if sequence_dna[i:i+3] == "AAA" or sequence_dna[i:i+3] ==  "AAG": sequence_prot_3 += "K"
    if sequence_dna[i:i+3] == "AAT" or sequence_dna[i:i+3] ==  "AAC": sequence_prot_3 += "N"
    if sequence_dna[i:i+3] == "ATG": sequence_prot_3 += "M"
    if sequence_dna[i:i+3] == "GAT" or sequence_dna[i:i+3] ==  "GAC": sequence_prot_3 += "D"
    if sequence_dna[i:i+3] == "TTT" or sequence_dna[i:i+3] ==  "TTC": sequence_prot_3 += "F"
    if sequence_dna[i:i+3] == "TGT" or sequence_dna[i:i+3] ==  "TGC": sequence_prot_3 += "C"
    if sequence_dna[i:i+3] == "CCT" or sequence_dna[i:i+3] ==  "CCC" or sequence_dna[i:i+3] ==  "CCA" or sequence_dna[i:i+3] ==  "CCG": sequence_prot_3 += "P"
    if sequence_dna[i:i+3] == "CAA" or sequence_dna[i:i+3] ==  "CAG": sequence_prot_3 += "Q"
    if sequence_dna[i:i+3] == "TCT" or sequence_dna[i:i+3] ==  "TCC" or sequence_dna[i:i+3] ==  "TCA" or sequence_dna[i:i+3] ==  "TCG" or sequence_dna[i:i+3] ==  "AGT" or sequence_dna[i:i+3] ==  "AGC": sequence_prot_3 += "S"
    if sequence_dna[i:i+3] == "GAA" or sequence_dna[i:i+3] ==  "GAG": sequence_prot_3 += "E"
    if sequence_dna[i:i+3] == "ACT" or sequence_dna[i:i+3] ==  "ACC" or sequence_dna[i:i+3] ==  "ACA" or sequence_dna[i:i+3] ==  "ACG": sequence_prot_3 += "T"
    if sequence_dna[i:i+3] == "GGT" or sequence_dna[i:i+3] ==  "GGC" or sequence_dna[i:i+3] ==  "GGA" or sequence_dna[i:i+3] ==  "GGG": sequence_prot_3 += "G"
    if sequence_dna[i:i+3] == "TGG": sequence_prot_3 += "W"
    if sequence_dna[i:i+3] == "CAT" or sequence_dna[i:i+3] ==  "CAC": sequence_prot_3 += "H"
    if sequence_dna[i:i+3] == "TAT" or sequence_dna[i:i+3] ==  "TAC": sequence_prot_3 += "Y"
    if sequence_dna[i:i+3] == "ATT" or sequence_dna[i:i+3] ==  "ATC" or sequence_dna[i:i+3] ==  "ATA": sequence_prot_3 += "I"
    if sequence_dna[i:i+3] == "GTT" or sequence_dna[i:i+3] ==  "GTC" or sequence_dna[i:i+3] ==  "GTA" or sequence_dna[i:i+3] ==  "GTG": sequence_prot_3 += "V"
    if sequence_dna[i:i+3] == "TAA" or sequence_dna[i:i+3] ==  "TGA" or sequence_dna[i:i+3] ==  "TAG": sequence_prot_3 += "*"

print "<p><b>Исходная последовательность ДНК (",n, "нуклеотидов):</b></p>"
for i in range(0, len(sequence_dna), 50):
    print "<p><h3>", sequence_dna[i:i+10], " ", sequence_dna[i+10:i+20], " ", sequence_dna[i+20:i+30], " ", sequence_dna[i+30:i+40], " ", sequence_dna[i+40:i+50], "</h3></p>"

print "<p>Аминокислотная последовательность по 1-ой рамке считания:</p>"
for i in range(0, len(sequence_prot_1), 50):
    print "<p><h5>", sequence_prot_1[i:i+10], " ", sequence_prot_1[i+10:i+20], " ", sequence_prot_1[i+20:i+30], " ", sequence_prot_1[i+30:i+40], " ", sequence_prot_1[i+40:i+50], "</h5></p>"
print "<p>Аминокислотная последовательность по 2-ой рамке считания:</p>"
for i in range(0, len(sequence_prot_2), 50):
    print "<p><h5>", sequence_prot_2[i:i+10], " ", sequence_prot_2[i+10:i+20], " ", sequence_prot_2[i+20:i+30], " ", sequence_prot_2[i+30:i+40], " ", sequence_prot_2[i+40:i+50], "</h5></p>"
print "<p>Аминокислотная последовательность по 3-ей рамке считания:</p>"
for i in range(0, len(sequence_prot_3), 50):
    print "<p><h5>", sequence_prot_3[i:i+10], " ", sequence_prot_3[i+10:i+20], " ", sequence_prot_3[i+20:i+30], " ", sequence_prot_3[i+30:i+40], " ", sequence_prot_3[i+40:i+50], "</h5></p>"


print("""</body>
        </html>""")