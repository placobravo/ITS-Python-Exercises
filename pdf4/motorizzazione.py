automobili = {
    "veicolo1": {"colore": "blu", "modello": "alfa", "cilindrata": 3500},
    "veicolo2": {"colore": "rosso", "modello": "panda", "cilindrata": 2000},
    "veicolo3": {"colore": "nero", "modello": "lamborghini", "cilindrata": 8000},
    "veicolo4": {"colore": "grigio", "modello": "audi_a1", "cilindrata": 2500},
}

counter = 0
for x in automobili:
    if automobili[x]["cilindrata"] > 3000:
        print("il", x, "deve pagare il bollo!")
        counter += 1

print(
    counter,
    "macchina" if counter == 1 else "macchine",
    "in totale",
    "deve" if counter == 1 else "devono",
    "pagare il bollo!",
)
