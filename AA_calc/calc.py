#!/usr/bin/python
# coding: utf8
import cgi
import string
form = cgi.FieldStorage()
sequence = form.getfirst("sequence", "0") #Забрал данные, введенные в форму в редакторе html из панели управления
sequence = sequence.upper()


print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <link rel="stylesheet" type="text/css" href="calc.css">
            <title>Обработка данных форм</title>
        </head>
        <body>""")
print("<h2>Результаты:</h2>")
A = 0 #Пременные для подсчета аминокислот
R = 0
N = 0
D = 0
C = 0
E = 0
Q = 0
G = 0
H = 0
I = 0
L = 0
K = 0
M = 0
F = 0
P = 0
S = 0
T = 0
W = 0
Y = 0
V = 0
massA = 71.08 #Массы аминокислотных остатков (MW-H2O)
massR = 156.2
massN = 114.1
massD = 115.08
massC = 103.14
massE = 129.11
massQ = 128.13
massG = 57.05
massH = 137.14
massI = 113.16
massL = 113.16
massK = 128.17
massM = 131.19
massF = 147.17
massP = 97.11
massS = 87.08
massT = 101.1
massW = 186.21
massY = 163.17
massV = 99.13
for i in sequence:
 if i == "A" or i == "a": A = A + 1
 if i == "R" or i == "r": R = R + 1
 if i == "N" or i == "n": N = N + 1
 if i == "D" or i == "d": D = D + 1
 if i == "C" or i == "c": C = C + 1
 if i == "E" or i == "e": E = E + 1
 if i == "Q" or i == "q": Q = Q + 1
 if i == "G" or i == "g": G = G + 1
 if i == "H" or i == "h": H = H + 1
 if i == "I" or i == "i": I = I + 1
 if i == "L" or i == "l": L = L + 1
 if i == "K" or i == "k": K = K + 1
 if i == "M" or i == "m": M = M + 1
 if i == "F" or i == "f": F = F + 1
 if i == "P" or i == "p": P = P + 1
 if i == "S" or i == "s": S = S + 1
 if i == "T" or i == "t": T = T + 1
 if i == "W" or i == "w": W = W + 1
 if i == "Y" or i == "y": Y = Y + 1
 if i == "V" or i == "v": V = V + 1
Sum = A + R + N + D + C + E + Q + G + H + I + L + K + M + F + P + S + T + W + Y + V
WeightMass = massA*A + massR*R + massN*N + massD*D + massC*C + massE*E + massQ*Q + massG*G + massH*H + massI*I + massL*L + massK*K + massM*M + massF*F + massP*P + massS*S + massT*T + massW*W + massY*Y + massV*V + 18 #Масса белка исходя из последовательности
Extintion = 1490*Y + 5500*W + 125*C
Absorbance_1mgml = float(Extintion)/float(WeightMass)

percentA = float(A)/float(Sum)*100
percentR = float(R)/float(Sum)*100
percentN = float(N)/float(Sum)*100
percentD = float(D)/float(Sum)*100
percentC = float(C)/float(Sum)*100
percentE = float(E)/float(Sum)*100
percentQ = float(Q)/float(Sum)*100
percentG = float(G)/float(Sum)*100
percentH = float(H)/float(Sum)*100
percentI = float(I)/float(Sum)*100
percentL = float(L)/float(Sum)*100
percentK = float(K)/float(Sum)*100
percentM = float(M)/float(Sum)*100
percentF = float(F)/float(Sum)*100
percentP = float(P)/float(Sum)*100
percentS = float(S)/float(Sum)*100
percentT = float(T)/float(Sum)*100
percentW = float(W)/float(Sum)*100
percentY = float(Y)/float(Sum)*100
percentV = float(V)/float(Sum)*100

print("<p><b>Исходная последовательность:</b></p>")
for i in range(0, len(sequence), 50):
    print "<p><h3>", sequence[i:i+10], " ", sequence[i+10:i+20], " ", sequence[i+20:i+30], " ", sequence[i+30:i+40], " ", sequence[i+40:i+50], "</h3></p>"


#print('<p>Содержание G = <b>%.1f %%</b></p>' % (percent_G))


print("<p>Всего аминокислот: <b>%i</b> </p>"  % (Sum))
print("<p>Васса белка: <b>%.0f</b> Da </p>"  % (WeightMass))
print("<p>Коэффициент экстинкции на 280 нм: <b>%i</b> 1/М/см</p>"  % (Extintion))
print('<p>Поглощение на 280 нм расвора белка 1 мг/мл (0.1%%): <b>%.2f</b></p>' % Absorbance_1mgml)
print("<p><b>Аминокислотный состав:</b></p>")
print('<p>Ala (A)   %i\t %.1f%%</p>' % (A, percentA))
print('<p>Arg (R)   %i\t %.1f%%</p>' % (R, percentR))
print('<p>Asn (N)   %i\t %.1f%%</p>' % (N, percentN))
print('<p>Asp (D)   %i\t %.1f%%</p>' % (D, percentD))
print('<p>Cys (C)   %i\t %.1f%%</p>' % (C, percentC))
print('<p>Glu (E)   %i\t %.1f%%</p>' % (E, percentE))
print('<p>Gln (Q)   %i\t %.1f%%</p>' % (Q, percentQ))
print('<p>Gly (G)   %i\t %.1f%%</p>' % (G, percentG))
print('<p>His (H)   %i\t %.1f%%</p>' % (H, percentH))
print('<p>Ile (I)   %i\t %.1f%%</p>' % (I, percentI))
print('<p>Leu (L)   %i\t %.1f%%</p>' % (L, percentL))
print('<p>Lys (K)   %i\t %.1f%%</p>' % (K, percentK))
print('<p>Met (M)   %i\t %.1f%%</p>' % (M, percentM))
print('<p>Phe (F)   %i\t %.1f%%</p>' % (F, percentF))
print('<p>Pro (P)   %i\t %.1f%%</p>' % (P, percentP))
print('<p>Ser (S)   %i\t %.1f%%</p>' % (S, percentS))
print('<p>Thr (T)   %i\t %.1f%%</p>' % (T, percentT))
print('<p>Trp (W)   %i\t %.1f%%</p>' % (W, percentW))
print('<p>Tyr (Y)   %i\t %.1f%%</p>' % (Y, percentY))
print('<p>Val (V)   %i\t %.1f%%</p>' % (V, percentV))
print('<p>Число положительно заряженных остатков (Arg и Lys):   %i</p>' % (R+K))
print('<p>Число отрицательно заряженных остатков (Asp и Glu):   %i</p>' % (D+E))

print("""</body>
        </html>""")
