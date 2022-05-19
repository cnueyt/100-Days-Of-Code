liste = ["a","b","c","d","e"]
oteleme = int(input("öteleme sayısı gir:  \n"))
yeni_kelime = ""
for harf in liste:
    konum = liste.index(harf)
    yeni_konum = konum + oteleme
    yeni_harf = liste[yeni_konum]
    yeni_kelime += yeni_harf
    print(yeni_kelime)
    
print(yeni_kelime)