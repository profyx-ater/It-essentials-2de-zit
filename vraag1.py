# naam: Robbe Profeta
# klas: 1 TINH
import random


def main():
    aantal_verjaardagen = int(input("Hoeveel verjaardagen wil je genereeren? (max. 100) "))
    while aantal_verjaardagen < 0 or aantal_verjaardagen > 100:
        aantal_verjaardagen = int(input("Hoeveel verjaardagen wil je genereeren? (max. 100) "))

    maanden = ['Januari;31', 'Februari;29', 'Maart;31', 'April;30', 'Mei;31', 'Juni;30',
               'Juli;31', 'Augustus;31', 'September;30', 'Oktober;31', 'November;30', 'December;31']
    genereerVerjaardagen(maanden, aantal_verjaardagen)


def genereerVerjaardagen(maanden, aantal_verjaardagen):
    maandNaam = delenMaanden(maanden)
    maandAantalDagen = delenDagen(maanden)
    genereerdeMaand = []
    genereerdeDag = []
    for i in range(aantal_verjaardagen):
        random_maand = random.randint(1, len(maandNaam))
        genereerdeMaand.append(maandNaam[random_maand - 1])
        hoeveel_dagen_in_maand = maandAantalDagen[random_maand - 1]
        random_dag = random.randint(1, int(hoeveel_dagen_in_maand))
        genereerdeDag.append(random_dag)
    verjaardagen = PlaatsVerjaardagenOpScherm(genereerdeMaand, genereerdeDag)
    aantalVerjaardagenPerMaand(genereerdeMaand, maandNaam)
    verjaardagFrequentie(verjaardagen)


def verjaardagFrequentie(verjaardagen):
    verjaardagenAlGepaseerd = []
    aantalkeerGepaseerd = []
    for i in range(len(verjaardagen)):
        for j in range(len(verjaardagen)):
            if verjaardagenAlGepaseerd.count(verjaardagen[i]) == 0:
                verjaardagenAlGepaseerd.append(verjaardagen[i])
                aantalkeerGepaseerd.append(1)
            else:
                plaats = verjaardagenAlGepaseerd.index(verjaardagen[i])
                tijdelijkgetal = aantalkeerGepaseerd[plaats]
                tijdelijkgetal += 1

    indexHoogstedag = 0
    hoogstegetal = 0
    aantalgepaseerd = 0
    for x in range(len(aantalkeerGepaseerd)):
        if int(aantalkeerGepaseerd[x]) > hoogstegetal:
            indexHoogstedag = x
            aantalgepaseerd = aantalkeerGepaseerd[x]
    print(f"de verjaardag die het vaakst voorkomt is: {verjaardagenAlGepaseerd[indexHoogstedag]}")
    print(f"Deze verjaardag komt {aantalgepaseerd} keer voor.")


def aantalVerjaardagenPerMaand(genereerdeMaand, maandNaam):
    print("Aaantal per maand:")
    aantalVerjaardagenPerMaandLijst = []
    for lijstVullen in range(12):
        aantalVerjaardagenPerMaandLijst.append(0)
    for i in range(len(genereerdeMaand)):
        for j in range(len(maandNaam)):
            if genereerdeMaand[i] == maandNaam[j]:
                tijdelijkAantal = aantalVerjaardagenPerMaandLijst[j]
                tijdelijkAantal += 1
                aantalVerjaardagenPerMaandLijst[j] = tijdelijkAantal

    for x in range(len(maandNaam)):
        aantalVerjaardagen = aantalVerjaardagenPerMaandLijst[x]
        sterren = ""
        for j in range(aantalVerjaardagen):
            sterren += "*"
        print(f"{maandNaam[x]} {sterren}")


def PlaatsVerjaardagenOpScherm(genereerdeMaand, genereerdeDag):
    print("De genereerde verjaardagen zijn: ")
    verjaardagen = []
    for i in range(len(genereerdeMaand)):
        verjaardagen.append(f"{genereerdeDag[i]} {genereerdeMaand[i].lower()[0:3]}")
        print(f"{genereerdeDag[i]} {genereerdeMaand[i].lower()[0:3]}")
    return verjaardagen


def delenMaanden(maanden):
    lijstNaam = []
    for i in range(len(maanden)):
        maandNaam = maanden[i].split(";")
        lijstNaam.append(maandNaam[0])
    return lijstNaam


def delenDagen(maanden):
    lijstDagen = []
    for i in range(len(maanden)):
        maandFagen = maanden[i].split(";")
        lijstDagen.append(maandFagen[1])
    return lijstDagen


if __name__ == '__main__':
    main()
