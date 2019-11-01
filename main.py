import json, datetime

standaardPrijsUur = 0.30

def intOVChek(OVKaartNummer):
    try:
        OVKaartNummer = int(OVKaartNummer)
        if OVKaartNummer < 0:
            return 'negatief'
        elif kluisCheck(OVKaartNummer)[1]:
            return OVKaartNummer
        else:
            return 'geenOV'
    except:
        return 'geenInt'


def kluisCheck(kaartNummer):
    """Controleren of een kaartnummer al gebruikt maakt van een kluis."""
    with open("fietsenstallingen.json", 'r', encoding='utf-8') as infile:
        kluisjes = json.load(infile)
    for x in kluisjes:
        if kaartNummer == x['kaartNummer']:
            resultaat = ["U mag maar 1 kluis in gebruik hebben. Leeg uw kluis eerst voordat u een nieuwe aanvraagt", True]
            return resultaat
    resultaat = ["", False]
    return resultaat

def kluisIndex(kaartNummer):
    """controleren of een kaartnummer een kluisje gebruikt en de index van kluisje terug geven"""
    legeKluizen = 0
    with open("fietsenstallingen.json", 'r', encoding='utf-8') as infile:
        kluisjes = json.load(infile)
    for x in kluisjes:
        if kaartNummer == x['kaartNummer']:
            resultaat = x['kluisNummer']
            return resultaat
        else:
            legeKluizen += 1
            if legeKluizen == len(kluisjes):
                resultaat = False
                return resultaat

def nieuweKluis(kaartNummer):
    """
    Nieuwe kluis aanmaken met opgegeven kaartnummer
    JSON file lezen, dictionary van kaartnummer, stallingstijd en eerstvolgende vrije kluis toevoegen aan lijst toevoegen
    daarna terug schrijven naar de JSON file met de 'w' parameter zodat alles eerst geleegd wordt.
    """
    teller = 1
    with open("fietsenstallingen.json", 'r', encoding='utf-8') as infile:
        kluisjes = json.load(infile)
    test = kluisCheck(kaartNummer)
    if test[1]:
        return test[0]
    dictionary = huidigeDatum()
    dictionary['bezet'] = True
    dictionary['kluisNummer'] = len(kluisjes) + 1
    legeLijst = []
    for x in kluisjes:
        legeLijst.append(x['kluisNummer'])
    for x in kluisjes:
        if teller in legeLijst:
            teller += 1
            continue
        else:
            dictionary['kluisNummer'] = teller
            break
    dictionary['kaartNummer'] = kaartNummer
    kluisjes.append(dictionary)
    resultaat = "U heeft kluisje: {}".format(dictionary['kluisNummer'])
    with open("fietsenstallingen.json", 'w', encoding='utf-8') as outfile:
        json.dump(kluisjes, outfile, ensure_ascii=False, indent=4)
    return resultaat


def kluisInleveren(kaartnummer):
    """
    Dictionary entry verwijderen uit lijst in JSON bestand.
    Door lijst heen loopen totdat kaartnummer is gevonden.
    Die dictionary uit de lijst poppen
    Nieuwe verkorte lijst naar de JSON schrijven met 'w' parameter zodat de file eerst geleegd wordt.
    """
    with open("fietsenstallingen.json", 'r', encoding='utf-8') as infile:
        kluisjes = json.load(infile)
    index = kluisIndex(kaartnummer)
    if isinstance(index, str):
        return index
    else:
        index -= 1
    kluisjes.pop(index)
    with open("fietsenstallingen.json", 'w', encoding='utf-8') as outfile:
        json.dump(kluisjes, outfile, ensure_ascii=False, indent=4)
    tekst = "Uw kluis is ingeleverd"
    return tekst

def huidigePrijs(kaartNummer):
    """Huidige prijs berekenen per minuut door de huidige tijd in minuten min de tijd van stalling in minuten keer de prijs per minuut te doen."""
    with open("fietsenstallingen.json", 'r', encoding='utf-8') as infile:
        kluisjes = json.load(infile)
    for x in kluisjes:
        if kaartNummer == x["kaartNummer"]:
            prijs = (totaalMinuten(huidigeDatum()) - totaalMinuten(x)) * standaardPrijsUur / 60
            return prijs
    geenKluis = "U heeft geen kluis in gebruik en heeft dus ook geen kosten"
    return geenKluis

def totaalMinuten(datumDictionary):
    """Totale aantal minuten die verstreken zijn sinds 0/0/0/0/0 (J/M/D/U/M) berekenen tot de gegeven datum."""
    #lijst zodat de som makkelijk kan worden berekend door te slicen en de sum te berekenen.
    dagenInMaanden = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    som = sum(dagenInMaanden[:datumDictionary['stallingsMaand'] + 1])
    antMinuten = ((((som + datumDictionary['stallingsJaar'] * 365 + datumDictionary['stallingsJaar'] // 4) + datumDictionary['stallingsDag']) * 24 + datumDictionary["stallingsUur"]) * 60 + datumDictionary['stallingsMinuut'])  # ant jaar * 365 + 1 dag per vier hele jaren + ant dagen in huidige jaar
    return antMinuten

def huidigeDatum():
    """Returnd de huidige datum in een dictionary volgens het volgende format Jaar/Maand/Dag/Uur/Minuut in cijfers."""
    vandaag = datetime.datetime.today()
    #dictionary om looping te voorkomen
    maanden = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}
    huidigeMaand, huidigeDag, huidigeJaar, huidigeUur, huidigeMinuut = vandaag.strftime('%b'), vandaag.strftime('%d'), vandaag.strftime('%Y'), vandaag.strftime("%H"), vandaag.strftime('%M')
    huidigeMaandNummer = maanden[huidigeMaand]
    datumDictionary = {
        "bezet": False,
        "kaartNummer": 0,
        "kluisNummer": 0,
        "stallingsJaar": int(huidigeJaar),
        "stallingsMaand": int(huidigeMaandNummer),
        "stallingsDag": int(huidigeDag),
        "stallingsUur": int(huidigeUur),
        "stallingsMinuut": int(huidigeMinuut)
    }
    return datumDictionary

def stalTijd(kaartnummer):
    """Berekent de aantal verstreken minuten sinds de tijd van stalling bij een kluisje dat gekoppelt is aan een gegeven kaartnummer."""
    locatie, teller = 0, 0
    with open('fietsenstallingen.json', 'r', encoding='utf-8') as infile:
        kluisjes = json.load(infile)
    for x in kluisjes:
        if kaartnummer == x['kaartNummer']:
            locatie = kluisjes.index(x)
        else:
            teller += 1
    if teller == len(kluisjes):
        bericht = "U heeft geen kluisje in gebruik\n"
        return bericht
    stallingsTijd = totaalMinuten(kluisjes[locatie])
    duur = int(totaalMinuten(huidigeDatum())- stallingsTijd)
    return duur