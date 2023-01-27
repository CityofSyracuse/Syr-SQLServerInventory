import pyodbc
import urllib
from sqlalchemy import create_engine

class SQLConnector(object):
    def __init__(self, host_ip, db, user, pwd, driver="{SQL Server}", conn_type="sql_alchemy"):
        """Class that connects to a database using pyodbc.
        Contains a few helper functions to maintain that."""
        if conn_type == "sql_alchemy":
            params = urllib.parse.quote_plus(f'DRIVER={driver};SERVER={host_ip};DATABASE={db};UID={user};PWD={pwd}')
            self._engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)
            self._conn = self._engine.connect()
        else:
            self._engine = None
            self._conn = pyodbc.connect(f'DRIVER={driver};SERVER={host_ip};DATABASE={db};UID={user};PWD={pwd}')


    def get_connection(self):
        return self._conn


    def get_engine(self):
        return self._engine


    def close_connection(self):
        self._conn.close()