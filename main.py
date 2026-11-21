print()
print("========== EXPENSE TRACKER ==========")
print()
print("1) Aggiungi entrata")
print("2) Aggiungi spesa")
print("3) Visualizza movimenti")
print("4) Calcola saldo")
print("5) Salva su un file CSV")
print("0) Esci")
print()
print("=====================================")

scelta = -1
movimenti = []
while scelta != 0:
    scelta = int(input("Scegli cosa vuoi fare: "))
    if scelta == 0:
        print("Grazie per aver utilizzato EXPENSE TRACKER ")
    elif scelta == 1:
        descrizione = input("Descrizione Entrata: ")
        importo = float(input("Importo: "))
        print(f"Entrata registrata: {descrizione} = {importo:.2f} €")
        movimento = {
            "tipo": "Entrata",
            "descrizione": descrizione,
            "importo": importo
        }
        movimenti.append(movimento)
    elif scelta == 2:
        descrizione = input("Descrizione Spesa: ")
        importo = float(input("Importo: "))
        print(f"Spesa registrata: {descrizione} = {importo:.2f} €")
        movimento = {
            "tipo": "Spesa",
            "descrizione": descrizione,
            "importo": importo
        }
        movimenti.append(movimento)
    elif scelta == 3:
        print("===== MOVIMENTI REGISTRATI =====")
        for movimento in movimenti:
            print(f"{movimento["tipo"]} - {movimento["descrizione"]} : {movimento["importo"]:.2f}€")

    elif scelta == 4:
        saldo = 0

        for movimento in movimenti:
            if movimento["tipo"] == "Entrata":
                saldo += movimento["importo"]
            else:
                saldo -= movimento["importo"]

        print("===== SALDO DISPONIBILE =====")
        print(f"Saldo attuale: {saldo:.2f} €")