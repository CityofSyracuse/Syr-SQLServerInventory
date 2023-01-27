from db_connection.sql_connector import SQLConnector
from db_connection.querier import Querier
import os
import pandas as pd


def get_db_creds(fname):

    with open(f"./db/{fname}", "r") as f:
        return {l.split("=")[0].rstrip(): l.split("=")[1].rstrip() for l in f.readlines()}


def get_query_text(fname):

    with open(f"./{fname}", "r") as f:
        return f.read()


def main():

    OUT_FNAME = "dbs_by_server.xlsx"

    dfs = {}
    for fname in os.listdir("./db"):
        creds = get_db_creds(fname)
        if fname != "template.txt":
            connection = SQLConnector(creds["server_ip"], creds["db"], creds["user"], creds["pwd"])
            qer = Querier(connection.get_connection())
            q = get_query_text("query.sql")
            dfs[fname] = qer.perform_query(q)
            connection.close_connection()

    writer = pd.ExcelWriter(OUT_FNAME, engine='xlsxwriter')
    for serv_name, data in dfs.items():
        data.to_excel(writer, sheet_name=serv_name, index=False)
    writer.close()


if __name__ == "__main__":
    main()