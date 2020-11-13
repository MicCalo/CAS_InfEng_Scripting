# CAS_InfEng_Scripting
Gruppe 4 Immobilien Brooklyn NY
Datenquellen:
- [Verkaufspreise Grundstücke](https://www1.nyc.gov/site/finance/taxes/property-rolling-sales-data.page)
- [Kriminalität](https://www1.nyc.gov/site/nypd/stats/crime-statistics/citywide-crime-stats.page)
- [Schulen](https://data.cityofnewyork.us/Education/Brooklyn-Schools/bkjd-kr4k)
- [Kitas](https://data.cityofnewyork.us/Health/Childcare-Centers/tdif-34xu)

# Installation 

The following instructions are for VS Code with the python and yupiter extension installed.

## Create a python environment
Open a terminal in the root path of the project and create a new Python environment in the ``env`` directory.

```
c:\python39\python.exe -n venv env
```

Python 3.7/3.8 may work as well.

## Select the Python interpreter

Open command palette <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> in VS Code and select `Python: select interpreter`.  Choose the Python executable in the previously created directory.

## Open a Python terminal

Use the command `Python: Create Terminal` to open a terminal where the python environment is already applied.

## Install libraries

```
pip install -t requirements.txt
```

