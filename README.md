## Informazioni sul progetto
Indagine EDIT si pone l'obiettivo di rendere fruibili i dati raccolti dalla regione Toscana in materia di incidenti stradali.
## Guida all'utilizzo

### Prerequisiti

- [Python](https://www.python.org/)

### Installazione
- Impostare la variabile di ambiente `SECRET_KEY`.
- Impostare le variabili di ambiente `ALLOWED_HOSTS` e `CORS_ALLOWED_ORIGINS` con l'indirizzo ip del backend e del frontend rispettivamente.
- Avviare un virtual enviroment (e.g. [venv](https://docs.python.org/3/library/venv.html)).
- Eseguire `pip install -r requirements.txt`.

### Avvio
- Eseguire `python manage.py runserver`.