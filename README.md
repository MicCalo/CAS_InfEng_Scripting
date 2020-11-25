# CAS_InfEng_Scripting
Gruppe 4 Immobilien Brooklyn NY
Datenquellen:
- [Verkaufspreise Grundstücke](https://www1.nyc.gov/site/finance/taxes/property-rolling-sales-data.page)
- [Kriminalität](https://www1.nyc.gov/site/nypd/stats/crime-statistics/citywide-crime-stats.page)
- [Schulen](https://data.cityofnewyork.us/Education/Brooklyn-Schools/bkjd-kr4k)
- [Kitas](https://data.cityofnewyork.us/Health/Childcare-Centers/tdif-34xu)

# Installation

Um die Yupiter Notebooks möglichst einfach laufen zu lassen, kann ein entsprechender Docker Container gebaut und gestaret werden. Das geht sehr einfach mit nur einem Befehl.

Der Container basiert auf der Anaconda Version 2020.07 und enthält die noch benötigten Python Bibliotheken.

## Voraussetzungen

- Windows, Mac or Linux OS
- Docker installiert
- Bash Shell wenn ein Mac oder Linux verwendet wird
- CMD oder Powershell unter Windows
- Browser
# Start

## Mac, Linux

Ins Root Verzeichnis des Projekts wechseln

    cd <VERZEICHNIS_NAME>

Run aufrufen

    ./run.sh

Unter Umständen ist `run.sh` nicht ausführbar

    chmod +x run.sh
    ./run.sh

## Windows

### CMD

Ins Root Verzeichnis des Projekts wechseln

    cd <VERZEICHNIS_NAME>

Run aufrufen

    run

### Powershell

Ins Root Verzeichnis des Projekts wechseln

    cd <VERZEICHNIS_NAME>

Run aufrufen

    .\run.ps1