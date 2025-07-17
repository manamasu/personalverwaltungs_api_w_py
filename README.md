# Personalverwaltungs_API

Die Personalverwaltungs_API dient als Benutzerverwaltungs- und Authentifizierungs-Backend mit FastAPI,
PostgreSQL und JWT-Token.

## Features

- Benutzeregstrierung mit Password-Hashing
- Login & Logout mit JWT (Access & Refresh-Token)
- Refresh-Token Speicherung & Invalidierung
- Sichere APIs mit Zugriffsbeschränkung
- Optional: Vollständig dockerisiert Umgebung mit PostgreSQL (in progress)

---

## Tech-Stack

- **FastAPI** - Modernes Python Web-Framework
- **Pydantic** - Validierung & Konfiguration
- **SQLModel** - Ist ein ORM und basiert auf SQLAlchemy und Pydantic, wird hier genutzt für PostgreSQL
- **PostgreSQL** - Relationale Datenbank zur Speicherung
- **Passlib (bcrypt)** - sichere Passwort-hashes
- **Docker & Docker Compose** - Erlaubt das erstellen eines Image welches all die App-Dependencies/code enthält.

## Installation

### 1. Projekt lokal klonen

```bash
git clone https://github.com/manamasu/personalverwaltungs_api_w_py.git
cd *repo-name*
```

### 2. Virtuelle Umgebung erstellen und aktivieren

```bash
python -m venv venv
source venv/bin/activate # unter Windows: venv\Scripts\activate
```

### 3. Abhängigkeiten aus Requirements.txt installieren

```bash
pip install -r requirements.txt
```

### 4. .env Datei im Root-Folder erstellen

```bash
HOST=*Geeigneter_Host* - *Lokales_Beispiel: 127.0.0.1*
PORT=*Port_für_die_Anwendung*

SECRET_KEY=*Dein_persönlicher_jwt_secret_key*
ALGORITHM=*Hashing_Algorithmus*
ACCESS_TOKEN_EXPIRE_MINUTES=*GültigeZahlAnMinuten*
REFRESH_TOKEN_EXPIRE_DAYS=*GültigeZahlAnTagen*

POSTGRES_USER=*DeinDatenbankUser*
POSTGRES_PASSWORD=*DeinDatenbankPasswort*
POSTGRES_SERVER=*DeinDatenbankServer*
POSTGRES_PORT=*Datenbank_Port*
POSTGRES_DB=*DeinDatenbankName*
DATABASE_URL=*postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}* # Database_URL sollte so bestehen bleiben.
```

### 5. Anwendung starten

```bash
python run.py # unter Windows mit einer geeigneten Python-Version, auch folgendes möglich: py ./run.py
```
