# Import delle librerie necessarie
from textblob import TextBlob  # Libreria per l'analisi del sentiment
from datetime import datetime, timedelta  # Libreria per la gestione delle date
# Il sentiment è il punteggio calcolato attraverso TextBlob

# Funzione per mostrare le informazioni sul software
def info():
    """
    @brief Descrizione del software e del suo obiettivo.
    
    Questo software è pensato per gestire l'andamento di un luogo (come un ristorante/hotel/b&b e altro ancora) attraverso le recensioni.
    Lo scopo principale del seguente software è di aiutare i gestori di questi luoghi
    a monitorare e comprendere l'opinione dei clienti attraverso le stelle assegnate.
    Fornisce un'analisi del sentiment delle recensioni, identifica se il luogo sta peggiorando o migliorando
    e consente ai gestori di prendere decisioni informate per migliorare l'esperienza complessiva dei clienti.
    Il sentiment è il punteggio calcolato attraverso TextBlob.
    
    @note
    ATTENZIONE:
    SCRIVERE RECENSIONI IN INGLESE
    TextBlob, di default, analizza le recensioni in lingua inglese
    Se si immette una recensione in una lingua diversa, il sentiment calcolato sarà pari a 0
    TODO: Attraverso le API di Google Translate sarebbe possibile di tradurre in automatico tutte le recensioni
    TODO: Identificare i punti di forza e debolezza categorizzandoli per diverse categorie e assegnare delle stelle ad ogni categoria del luogo
    TODO: Attraverso framework come Selenium o BeatifulSoup si potrebbe automatizzare la raccolta delle recensioni trovate nel web
    """
    # Descrizione del software e del suo obiettivo
    print("Questo software è pensato per gestire l'andamento di un luogo (come un ristorante/hotel/b&b e altro ancora) attraverso le recensioni.")
    print("Lo scopo principale del seguente software è di aiutare i gestori di questi luoghi")
    print("a monitorare e comprendere l'opinione dei clienti attraverso le stelle assegnate.")
    print("Fornisce un'analisi del sentiment delle recensioni,  identifica se il luogo sta peggiorando o migliorando")
    print(" e consente ai gestori di prendere decisioni per migliorare l'esperienza complessiva dei clienti.")
    print(" ")
    print("ATTENZIONE: ")
    print("SCRIVERE RECENSIONI IN INGLESE")
    print("PER MAGGIORI INFORMAZIONI GUARDARE LA DOCUMENTAZIONE ALLEGATA")
    main()

def sceltaData():
    """
    @brief Funzione per la scelta della data della recensione.

    Mostra le opzioni per la scelta della data e acquisisce la scelta dell'utente.
    @return La data scelta è nel formato "YYYY-MM-DD".

    @note
    Se la scelta è 1, utilizza la data di oggi.
    Se la scelta è 2, l'utente inserisce manualmente la data.
    """
    print("Come vuoi gestire la data della recensione?")
    print("1. Utilizza la data di oggi")
    print("2. Inserisci manualmente la data")
    scelta = int(input("Scelta: "))
    if scelta == 1:
        # Utilizzo datetime.now() per ottenere la data e l'ora correnti come oggetto datetime
        # Quindi uso .strftime("%Y-%m-%d") per formattare questa data come una stringa nel formato "YYYY-MM-DD"
        # Questo mi servirà per dopo calcolare la tendenza in modo corretto
        data = datetime.now().strftime("%Y-%m-%d")
    elif scelta == 2:
        while True:
            data_input = input("Inserisci la data (YYYY-MM-DD): ")
            try:
                data = datetime.strptime(data_input, "%Y-%m-%d")
                # Utilizzo datetime.strptime() per convertire la stringa `data_input` in un oggetto datetime
                # Il formato "%Y-%m-%d" specifica che la stringa deve essere nel formato "YYYY-MM-DD"
                break
            except ValueError:
                print("Formato data non valido. Riprova.")
    else:
        # Se la scelta non è valida, utilizza la data di oggi
        print("Selezione non valida. Utilizzerà la data di oggi.")
        data = datetime.now().strftime("%Y-%m-%d")
    return data


def inserimento():
    """
    @brief Funzione per l'inserimento di una nuova recensione.

    Richiede all'utente di inserire il voto e la recensione, e salva la recensione nel file "recensioni.txt".
    Se la recensione è vuota, mostra un messaggio di errore.

    @note
    Il voto deve essere un numero intero tra 0 e 10.
    La recensione non può essere vuota.
    """
    # Richiede all'utente di inserire il voto e la recensione
    voto = int(input("Inserisci il voto da 0 a 10: "))
    recensione = input("Inserisci la recensione: ")
    if recensione.strip():
        # Se la recensione è vuota il metodo .strip() restituisce una stringa vuota
        # In Python una stringa vuota è uguale a FALSE
        data = sceltaData()
        # Salva la recensione nel file "recensioni.txt" e usa il delimitatore @
        with open("recensioni.txt", "a") as file:
            file.write(f"{data}@{voto}@{recensione}\n")
        print("Recensione salvata con successo!")
    else:
        # Se la recensione è vuota, mostra un messaggio di errore
        print("La recensione non può essere vuota. Riprova.")
    main()


def visualizzaTutto():
    """
    @brief Funzione per visualizzare tutte le recensioni presenti nel file "recensioni.txt".

    Legge ogni riga del file e mostra i dettagli della recensione.
    Gestisce il caso in cui il file non esiste o è vuoto.

    @note
    Se il file "recensioni.txt" non esiste o è vuoto, viene mostrato un messaggio di errore.
    """
    try:
        # Apre il file "recensioni.txt" in modalità di lettura
        with open("recensioni.txt", "r") as file:
            # Legge ogni riga del file e mostra i dettagli della recensione
            for line in file:
                data, voto, recensione = line.strip().split("@")
                print(f"Data: {data}, Voto: {voto}, Recensione: {recensione}")
    except FileNotFoundError:
        # Gestisce il caso in cui il file non esiste o è vuoto
        print("Il file recensioni.txt non esiste o è vuoto.")
    main()

# Funzione per analizzare il sentiment delle recensioni e calcolare la media dei voti
def analizzaSentiment():
    """
    @brief Funzione per analizzare il sentiment delle recensioni e calcolare la media dei voti.

    Legge ogni riga del file "recensioni.txt" e analizza il sentiment della recensione utilizzando TextBlob.
    Calcola e mostra la media del sentiment e dei voti, e le stelle attuali assegnate.
    Gestisce il caso in cui il file non esiste o è vuoto.

    @details
    Algoritmo:
    1. Inizializza le variabili punteggioTot (punteggio totale del sentiment), contaRecen (numero di recensioni) e votoTot (totale dei voti).
    2. Leggi ogni riga del file "recensioni.txt".
    3. Per ogni recensione, analizza il sentiment utilizzando TextBlob e calcola un punteggio normalizzato tra 0 e 10.
    4. Somma il voto e il punteggio del sentiment alle relative variabili totali.
    5. Calcola la media del sentiment e dei voti.
    6. Calcola la media tra la media del sentiment e la media dei voti per determinare le stelle da assegnare.
    7. Gestisce il caso in cui non ci sono recensioni o il file non esiste.

    @note
    Se non ci sono recensioni, viene mostrato un messaggio appropriato.
    """
    punteggioTot = 0  # Variabile per sommare i punteggi del sentiment
    contaRecen = 0  # Variabile per contare il numero di recensioni
    votoTot = 0  # Variabile per sommare i voti delle recensioni
    
    try:
        # Apre il file "recensioni.txt" in modalità di lettura
        with open("recensioni.txt", "r") as file:
            # Legge ogni riga del file e analizza il sentiment della recensione
            for line in file:
                data, voto, recensione = line.strip().split("@")
                
                # Utilizza TextBlob per analizzare il sentiment della recensione
                blob = TextBlob(recensione)
                # Assegna un punteggio alla recensione
                # Il punto assegnato varia da -1 (molto negativo) a 1 (molto positivo)
                
                # Convertiamo questo valore in una scala da 0 a 10
                score = ((blob.sentiment.polarity + 1) * 10) / 2
                
                # Somma il voto e il punteggio calcolato
                votoTot += int(voto)
                punteggioTot += score
                contaRecen += 1

        if contaRecen > 0:
            # Se ci sono recensioni, calcola la media del sentiment e dei voti
            # Per assegnare le stelle, calcoliamo la media tra la media del sentiment e la media dei voti,
            # in modo da dare un peso del 50% sia al voto che al sentiment calcolato in precedenza.
            mediasent = (punteggioTot / contaRecen) 
            print(f"Media del sentiment calcolata: {mediasent:.2f} su 10")
            mediaVoto = (votoTot / contaRecen)
            print(f"Media dei voti inseriti da utente: {mediaVoto:.2f} su 10")
            mediaSentVoto = (mediaVoto + mediasent) / 2
            print(f"Stelle attuali assegnate: {mediaSentVoto:.2f} su 10")
        else:
            print("Non ci sono recensioni da analizzare.")
    except FileNotFoundError:
        # Gestisce il caso in cui il file non esiste o è vuoto
        print("Il file recensioni.txt non esiste o è vuoto.")
    main()

# Funzione per visualizzare le migliori recensioni basate sul voto e sul sentiment
def visualizzaMigliori():
    """
    @brief Funzione per visualizzare le migliori recensioni basate sul voto e sul sentiment.

    Legge ogni riga del file "recensioni.txt" e calcola il punteggio basato sul voto e sul sentiment utilizzando TextBlob.
    Ordina le recensioni in ordine decrescente e mostra le migliori 5.
    Gestisce il caso in cui il file non esiste o è vuoto.

    @note
    Se non ci sono recensioni, viene mostrato un messaggio appropriato.
    """
    try:
        # Lista per memorizzare le recensioni
        recensioni = []
        with open("recensioni.txt", "r") as file:
            # Legge ogni riga del file e calcola il punteggio basato sul voto e sul sentiment (Punteggio calcolato attraverso TextBlob)
            for line in file:
                # Uso .strip() per rimuovere eventuali spazi all'inizio e alla fine della stringa letta dal file.
                # Uso .split('@') per dividere la stringa letta dal file utilizzando '@' come delimitatore.
                # Ho scelto '@' come delimitatore perché è stato utilizzato durante l'inserimento delle recensioni.
                data, voto, recensione = line.strip().split("@")
                
                # Utilizza TextBlob per analizzare il sentiment della recensione
                blob = TextBlob(recensione)
                # Assegna un punteggio alla recensione
                # Il punto assegnato varia da -1 (molto negativo) a 1 (molto positivo)
                # Convertiamo questo valore in una scala da 0 a 10
                score = ((blob.sentiment.polarity + 1) * 10) / 2
                
                # Aggiunge la recensione alla lista con voto e punteggio di sentiment
                recensioni.append((float(voto), recensione, score))

        if recensioni:
            # Ordina le recensioni in ordine decrescente e mostra le migliori 5
            recensioni.sort(reverse=True)
            print("Le recensioni migliori sono:")
            for i in range(min(5, len(recensioni))):
                media = (recensioni[i][0] + recensioni[i][2]) / 2
                print(f"Voto: {recensioni[i][0]}, Sentiment: {recensioni[i][2]}, Media: {media:.2f}, Recensione: {recensioni[i][1]}")
        else:
            # Se non ci sono recensioni, mostra un messaggio appropriato
            print("Non ci sono recensioni da visualizzare.")
    except FileNotFoundError:
        # Gestisce il caso in cui il file non esiste o è vuoto
        print("Il file recensioni.txt non esiste o è vuoto.")
    main()

# Funzione per visualizzare le peggiori recensioni basate sul voto e sul sentiment
def visualizzaPeggiori():
    """
    @brief Funzione per visualizzare le migliori recensioni basate sul voto e sul sentiment.

    Legge ogni riga del file "recensioni.txt" e calcola il punteggio basato sul voto e sul sentiment utilizzando TextBlob.
    Ordina le recensioni in ordine crescente e mostra le peggiori 5.
    Gestisce il caso in cui il file non esiste o è vuoto.

    @note
    Se non ci sono recensioni, viene mostrato un messaggio appropriato.
    """
    try:
        # Lista per memorizzare le recensioni
        recensioni = []
        with open("recensioni.txt", "r") as file:
            # Legge ogni riga del file e calcola il punteggio basato sul voto e sul sentiment
            for line in file:
                # Uso .strip() per rimuovere eventuali spazi all'inizio e alla fine della stringa letta dal file.
                # Uso .split('@') per dividere la stringa letta dal file utilizzando '@' come delimitatore.
                # Ho scelto '@' come delimitatore perché è stato utilizzato durante l'inserimento delle recensioni.

                data, voto, recensione = line.strip().split("@")
                
                # Utilizza TextBlob per analizzare il sentiment della recensione
                blob = TextBlob(recensione)
                # Assegna un punteggio alla recensione
                # Il punto assegnato varia da -1 a 1
                # Convertiamo questo valore in una scala da 0 a 10
                score = ((blob.sentiment.polarity + 1) * 10) / 2
                
                # Aggiunge la recensione alla lista con voto e punteggio calcolato
                recensioni.append((float(voto), recensione, score))

        if recensioni:
            # Ordina le recensioni in ordine crescente e mostra le peggiori 5
            recensioni.sort()
            print("Le recensioni peggiori sono:")
            for i in range(min(5, len(recensioni))):
                media = (recensioni[i][0] + recensioni[i][2]) / 2
                print(f"Voto: {recensioni[i][0]}, Sentiment: {recensioni[i][2]}, Media: {media:.2f}, Recensione: {recensioni[i][1]}")
        else:
            # Se non ci sono recensioni, mostra un messaggio appropriato
            print("Non ci sono recensioni da visualizzare.")
    except FileNotFoundError:
        # Gestisce il caso in cui il file non esiste o è vuoto
        print("Il file recensioni.txt non esiste o è vuoto.")
    main()

# Funzione per cercare recensioni in base a un criterio specifico
def ricerca():
    """
    @brief Funzione per cercare recensioni contenenti un termine specifico.

    Richiede all'utente di inserire un termine di ricerca e mostra tutte le recensioni che contengono quel termine.
    Gestisce il caso in cui il file non esiste o è vuoto.

    @note
    Se il termine di ricerca non è trovato in nessuna recensione, viene mostrato un messaggio appropriato.
    """
    # Richiede all'utente di inserire il criterio di ricerca
    criterio = input("Inserisci il criterio di ricerca (data, voto, parola_chiave): ").lower()
    if criterio == "data":
        # Cerca le recensioni per data
        data_ricerca = input("Inserisci la data di interesse (YYYY-MM-DD): ")
        with open("recensioni.txt", "r") as file:
            for line in file:
                data, voto, recensione = line.strip().split("@")
                if data == data_ricerca:
                    print(f"Data: {data}, Voto: {voto}, Recensione: {recensione}")
    elif criterio == "voto":
        # Cerca le recensioni per voto
        voto_ricerca = int(input("Inserisci il voto da cercare: "))
        with open("recensioni.txt", "r") as file:
            for line in file:
                data, voto, recensione = line.strip().split("@")
                if int(voto) == voto_ricerca:
                    print(f"Data: {data}, Voto: {voto}, Recensione: {recensione}")
    elif criterio == "parola_chiave":
        # Cerca le recensioni per parola chiave
        parola_chiave = input("Inserisci la parola chiave da cercare nella recensione: ")
        with open("recensioni.txt", "r") as file:
            for line in file:
                data, voto, recensione = line.strip().split("@")
                if parola_chiave.lower() in recensione.lower():
                    print(f"Data: {data}, Voto: {voto}, Recensione: {recensione}")
    else:
        # Se il criterio non è valido, mostra un messaggio di errore
        print("Criterio non valido.")
    main()

# Funzione per analizzare la tendenza del miglioramento delle recensioni negli ultimi 30 giorni
def tendenzaMiglioramento():
    """
    @brief Funzione per analizzare la tendenza di miglioramento delle recensioni.

    Analizza le recensioni degli ultimi 30 giorni e confronta la media dei voti e del sentiment con i 30 giorni precedenti.
    Determina se c'è una tendenza al miglioramento o peggioramento.

    @details
    Algoritmo:
    1. Leggi tutte le recensioni dal file "recensioni.txt".
    2. Filtra le recensioni degli ultimi 30 giorni e i 30 giorni precedenti.
    3. Calcola la media dei voti e del sentiment per entrambe le finestre temporali.
    4. Confronta le medie e determina se c'è un miglioramento o peggioramento.

    @note
    Se non ci sono recensioni sufficienti per l'analisi, viene mostrato un messaggio appropriato.
    """
    try:
        oggi = datetime.now()
        trenta_giorni_fa = oggi - timedelta(days=30)
        sessanta_giorni_fa = oggi - timedelta(days=60)

        recensioni_recenti = []
        recensioni_precedenti = []

        with open("recensioni.txt", "r") as file:
            for line in file:
                data, voto, recensione = line.strip().split("@")
                data_recensione = datetime.strptime(data, "%Y-%m-%d")
                blob = TextBlob(recensione)
                score = ((blob.sentiment.polarity + 1) * 10) / 2
                if trenta_giorni_fa <= data_recensione <= oggi:
                    recensioni_recenti.append((float(voto), score))
                elif sessanta_giorni_fa <= data_recensione < trenta_giorni_fa:
                    recensioni_precedenti.append((float(voto), score))

        if recensioni_recenti and recensioni_precedenti:
            media_voto_recenti = sum([r[0] for r in recensioni_recenti]) / len(recensioni_recenti)
            media_sentiment_recenti = sum([r[1] for r in recensioni_recenti]) / len(recensioni_recenti)
            media_recenti = (media_voto_recenti + media_sentiment_recenti) / 2

            media_voto_precedenti = sum([r[0] for r in recensioni_precedenti]) / len(recensioni_precedenti)
            media_sentiment_precedenti = sum([r[1] for r in recensioni_precedenti]) / len(recensioni_precedenti)
            media_precedenti = (media_voto_precedenti + media_sentiment_precedenti) / 2

            print(f"Media dei voti degli ultimi 30 giorni: {media_voto_recenti:.2f}")
            print(f"Media del sentiment degli ultimi 30 giorni: {media_sentiment_recenti:.2f}")
            print(f"Media complessiva degli ultimi 30 giorni: {media_recenti:.2f}")
            print(f"Media dei voti del mese scorso (60 giorni fa, fino a 30 giorni fa): {media_voto_precedenti:.2f}")
            print(f"Media del sentiment del mese scorso: {media_sentiment_precedenti:.2f}")
            print(f"Media complessiva del mese scorso: {media_precedenti:.2f}")

            if media_recenti > media_precedenti:
                print("La tendenza sta migliorando.")
            else:
                print("La tendenza sta peggiorando.")
        else:
            print("Non ci sono abbastanza recensioni per determinare la tendenza.")
    except FileNotFoundError:
        print("Il file recensioni.txt non esiste o è vuoto.")
    main()

# Funzione principale del programma che gestisce il menu e le scelte dell'utente
def main():
    """
    @brief Mostra il menù principale del programma.
    """
    print("Benvenuto in questo software sviluppato da Gioele Russo")
    print("Selezionare una voce:")
    print("0- Esci")
    print("1- Informazioni sul software")
    print("2- Inserisci recensione")
    print("3- Visualizza tutte le recensioni")
    print("4- Visualizza media del sentiment delle recensioni e assegna stelle")
    print("5- Visualizza le recensioni migliori in base al voto")
    print("6- Visualizza le recensioni peggiori in base al voto")
    print("7- Cerca una recensione")
    print("8- Tendenza negli ultimi 30 giorni")
    
    # Acquisisce la scelta dell'utente
    scelta = int(input())

    if scelta == 0:
        exit()
    elif scelta == 1:
        info()
    elif scelta == 2:
        inserimento()
    elif scelta == 3:
        visualizzaTutto()
    elif scelta == 4:
        analizzaSentiment()
    elif scelta == 5:
        visualizzaMigliori()
    elif scelta == 6:
        visualizzaPeggiori()
    elif scelta == 7:
        ricerca()
    elif scelta == 8:
        tendenzaMiglioramento()
    else:
        print("Selezione non valida. Riprova.")

# Esecuzione del programma principale
if __name__ == "__main__":
    main()
