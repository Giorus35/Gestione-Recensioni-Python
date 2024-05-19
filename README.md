# Gestione recensioni

## Descrizione del Software

Questo software è stato sviluppato per aiutare i gestori di luoghi come ristoranti, hotel, B&B e altri a monitorare e comprendere l'opinione dei clienti attraverso le recensioni. L'obiettivo principale è fornire un'analisi del sentiment delle recensioni, identificare se il luogo sta peggiorando o migliorando e consentire ai gestori di prendere decisioni informate per migliorare l'esperienza complessiva dei clienti. Il sentiment è il punteggio calcolato attraverso la libreria TextBlob.

**ATTENZIONE:**  
- SCRIVERE RECENSIONI IN INGLESE  
TextBlob, di default, analizza le recensioni in lingua inglese. Se si immette una recensione in una lingua diversa, il sentiment calcolato sarà pari a 0.
- Al primo avvio aspettare almeno 30 secondi per l'esecuzione
- Per maggiori informazioni guardare la documentazione
- È stato fornito un file di test chiamato "recensioni.txt"
## Funzionalità Principali

1. **Informazioni sul Software:** Visualizza le informazioni generali sul software e le sue funzionalità.
2. **Inserisci Recensione:** Permette di inserire nuove recensioni con un voto e una descrizione.
3. **Visualizza Tutte le Recensioni:** Mostra tutte le recensioni salvate.
4. **Analizza Sentiment:** Calcola la media del sentiment delle recensioni e assegna delle stelle in base ai risultati.
5. **Visualizza le Recensioni Migliori:** Mostra le migliori 5 recensioni in base al voto.
6. **Visualizza le Recensioni Peggiori:** Mostra le peggiori 5 recensioni in base al voto.
7. **Cerca Recensione:** Permette di cercare recensioni in base a un criterio specifico (data, voto, parola chiave).
8. **Tendenza Miglioramento:** Analizza la tendenza di miglioramento delle recensioni negli ultimi 30 giorni rispetto ai 30 giorni precedenti.

## Requisiti

- Python 3.9 o superiore (Attualmente non è stato testato per versioni precedenti)
- Libreria `TextBlob` 
- Libreria `DateTime`
## Installazione

1. Clona questo repository o scarica il codice sorgente.
2. Installa le dipendenze richieste eseguendo il comando:
   ```bash
   pip install textblob
   ```
   ```bash
   pip install DateTime
   ```
## Utilizzo

Per avviare il software, esegui il file Python principale:
```bash
python GestioneRecensioni.py
```
oppure 
```bash
python3 GestioneRecensioni.py
```

## TODO

- Integrare le API di Google Translate per tradurre automaticamente tutte le recensioni.
- Identificare i punti di forza e debolezza categorizzandoli per diverse categorie e assegnare delle stelle ad ogni categoria(es. Pulizia, Cibo, Servizio, Location etc...).
- Automatizzare la raccolta delle recensioni trovate sul web utilizzando framework come Selenium o BeautifulSoup.
- Creare interfaccia grafica semplice e intuitiva

## Autore

Questo software è stato sviluppato da Gioele Russo.

## Contatti

Per ulteriori informazioni, suggerimenti o segnalazioni di bug, contattare l'autore all'indirizzo email: gioele.russo@iispadovano.it

---
