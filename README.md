# Syr-SQLServerInventory

## Contacts:

|||
|-|-|
|*Author*|Trevor Grant|
|*Email*|Tgrant@syr.gov|
|*Last Updated*|01/27/2023|

## Introduction

Prior to planning database migrations the City of Syracuse is performing an inventory of the current SQL servers currently hosted on premise. Not only does CoS wish to know technical details of theese systems (number of tables, number of rows, how much total data is stored, etc), but also opoerational implications like potential end users as well as other data systems fed by these sources. This code serves as a quick and dirty way to ping these systems automatically to extract information about the technical details of these servers and the databases stored therein.

***Note: Database credentials **are not**, and **should not** be stored in this repository (for [hopoefully] obvious reasons), and need to be entered by the end user in order for this program to run successfully. A template file is stored in `./db` folder which should guide the user where the enter these credentials.***

***Additional Note: The machine that is running this script must be within network to connect to these servers.***
## Entrypoint and Execution.

The main entrypoint for the code is `main.py` (clever, I know). This file makes use of the other objects provided in this code (in `./db_connection` subfolder). Here is a rundown of what main does:

1. Reads through the files in the `./db` directory. 
2. Parses those files to create an ODBC connection.
3. Performs the query in the `query.sql` file.
4. Collates that information into the output file: `dbs_by_server.xlsx`.

## Installation and Running:

1. Download this code:

```git clone https://github.com/CityofSyracuse/Syr-CaminoAPIWrapperDataLake```

2. Navigate to this directory:

```cd <path/to/repository>```

3. Create a virtual environment:

```python -m venv venv```

4. Activate the environment:

(Windows):
```.\venv\Scripts\activate```
(Linux / Mac)
```source venv/bin/activate```

5. Install the requirements.

```pip install -r requirements.txt```

6. Go ahead and run the program.

```python main.py```

## Notes

None.