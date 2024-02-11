# Esercizio: generazione di dati sintetici
#
# Generare una finta anagrafica in cui ogni record deve disporre di nome, cognome, indirizzo, città, età, paese di origine.
#
# Utilizzare il modulo <faker> per la generazione dei dati, o in alternativa, combinazioni casuali di dati a partire da liste precompilate. Salvare i dati in formato csv utilizzando il modulo csv cambiando il separatore di default
#
# Ricaricare i dati dal file csv e generare un report sulla provenienza degli utenti e sul loro paese di origine
#
# calcolare l'età media
import random
import csv

nome = [
    "mario",
    "tonio",
    "beppe",
    "giovanni",
    "antonio",
    "mariobeppe",
    "canoffo",
    "osvaldo",
    "maolino",
    "tonello",
    "mariobabo",
    "carmelo",
]
cognome = [
    "toffo",
    "marioni",
    "scanovini",
    "palazzi",
    "bocchini",
    "tontino",
    "coatto",
    "panasoni",
    "ottante",
    "lucenti",
]
indirizzo = [
    "via viola",
    "via campo di marte",
    "piazza partigiani",
    "via giotto",
    "via dell'acqua",
    "piazza del popolo",
    "via del signore",
    "piazza santa",
    "via saturno",
]
citta = [
    "perugia",
    "firenze",
    "roma",
    "todi",
    "torino",
    "milano",
    "siena",
    "poppi",
    "savignano sul rubicone",
    "terni",
    "teramo",
]
eta = [random.randint(18, 70) for x in range(50)]
paese_di_origine = [
    "marte",
    "giove",
    "saturno",
    "mercurio",
    "venere",
    "terra",
    "urano",
    "nettuno",
]


def createPerson():
    return (
        random.choice(nome),
        random.choice(cognome),
        random.choice(indirizzo),
        random.choice(citta),
        random.choice(eta),
        random.choice(paese_di_origine),
    )


persone = []
eta_totale = 0
num_persone = 0

for i in range(11):
    persone.append(createPerson())

try:
    with open("faker.csv", "x") as csvfile:
        fakerwriter = csv.writer(csvfile, delimiter=",")
        fakerwriter.writerows(persone)
except FileExistsError:
    pass


with open("faker.csv", "r+") as csvfile:
    fakerreader = csv.reader(csvfile, delimiter=",")

    for item in fakerreader:
        print(
            "\nNome:\t\t\t",
            item[0],
            "\nCognome:\t\t",
            item[1],
            "\nIndirizzo:\t\t",
            item[2],
            "\nCittà:\t\t\t",
            item[3],
            "\nEtà:\t\t\t",
            item[4],
            "\nPaese di origine:\t",
            item[5],
        )
        eta_totale += int(item[4])
        num_persone += 1
    print("\n" * 5)

    print("L'età media è: %.2f anni. " % (eta_totale / num_persone))
