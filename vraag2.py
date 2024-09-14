# naam: Robbe Profeta
# klas: 1 TINH
def selecteer_activiteiten(activiteiten, naam):
    naamLetters = []
    mogelijkActiviteiten = []
    naamLetters.append(naam[0:1].lower())
    naamLetters.append(naam[len(naam) - 1:len(naam)].lower())
    even = 0
    middelsteletter = ""
    if len(naam) % 2 != 0:
        middelsteletter = naam[len(naam) // 2]
        even = 1
    for i in range(len(activiteiten)):
        hetWoord = []
        for letter in activiteiten[i]:
            hetWoord.append(letter.lower())
        if hetWoord.count(naamLetters[0]) != 0 and hetWoord.count(naamLetters[1]) != 0:
            if even == 1:
                if hetWoord.count(middelsteletter) == 0:
                    mogelijkActiviteiten.append(activiteiten[i])
            elif even == 0:
                mogelijkActiviteiten.append(activiteiten[i])

    return mogelijkActiviteiten


def bepaal_prijs_geselecteerde_activiteiten(geslecteerdeActiviteit, code):
    cijfers = []
    OmgezetteCode = str(code)
    cijfers.append(OmgezetteCode[1:2])
    cijfers.append(OmgezetteCode[3:4])
    volledigecijfer = cijfers[0] + cijfers[1]
    volledigecijferNaarInt = int(volledigecijfer)
    prijs = []
    for i in range(len(geslecteerdeActiviteit)):
        GratisActiviteit = 0
        for letter in geslecteerdeActiviteit[i].upper():
            if ord(letter) == volledigecijferNaarInt:
                GratisActiviteit = 1
            elif ord(letter.lower()) == volledigecijferNaarInt:
                GratisActiviteit = 1
        if GratisActiviteit == 1:
            prijs.append(0)
        else:
            prijs.append(8)
    return prijs


def main():
    activiteiten = ["Atletiek", "Batting Cage", "Boksen", "Biatlon", "Big game fishing", "Bouldering", "Cliff Jump",
                    "Core Stability", "Curling", "Dansen", "Darts", "E-Ziplining", "Iggy", "Lopen", "Golf", "Hexatech",
                    "Multiball", "Neo stadium", "Boogschieten", "ParaGliding", "Parkours", "Racen", "Roeien",
                    "Schaatsen",
                    "Shooting range", "Skiën", "Slackline", "SnowBoarden", "PXspeL Arena", "Speed Climbing",
                    "Suspended nets", "Trampoline", "Vissen", "Wielrennen", "Voetbal", "Vrije val", "Wingsuit"]

    # 1)
    naam = input("Geef je naam: ")
    while len(naam) < 3:
        naam = input("Geef je naam: ")

    # 2)
    code = int(input("Geef een 5-cijferige code voor de locker: "))
    while len(str(code)) < 5:
        code = int(input("Geef een 5-cijferige code voor de locker: "))

    geslecteerdeActiviteit = selecteer_activiteiten(activiteiten, naam)
    prijs = bepaal_prijs_geselecteerde_activiteiten(geslecteerdeActiviteit, code)

    print("\nLijst activteiten")
    for i in range(len(geslecteerdeActiviteit)):
        print(f"{geslecteerdeActiviteit[i]} {prijs[i]}")
    # 3)
    lijstMetActiviteiten = []
    woord = input("\nMaak een keuze uit de lijst van activiteiten. 'Stop' om te stoppen.\n")
    lijstMetActiviteiten.append(woord)
    while woord.lower() != "stop":
        woord = input()
        lijstMetActiviteiten.append(woord)

    te_betalen(lijstMetActiviteiten, geslecteerdeActiviteit, prijs)


def te_betalen(lijstMetActiviteiten, geselecteerdeActiviteit, prijs):
    betalen = 0
    for i in range(len(geselecteerdeActiviteit)):
        for j in range(len(lijstMetActiviteiten)):
            if geselecteerdeActiviteit[i].lower() == lijstMetActiviteiten[j].lower():
                betalen += prijs[i]
    print(f"Te betalen: {betalen}")


if __name__ == '__main__':
    main()
